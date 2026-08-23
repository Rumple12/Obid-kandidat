"use strict";

// Runs inside the pinned n8n container. It reads only execution tables and
// returns an allowlisted, credential-free projection. workflowData is never
// parsed or returned because it can contain private credential references.

const sqlite3 = require("/usr/local/lib/node_modules/n8n/node_modules/.pnpm/sqlite3@5.1.7/node_modules/sqlite3");
const { parse: parseFlatted } = require("/usr/local/lib/node_modules/n8n/node_modules/.pnpm/flatted@3.2.7/node_modules/flatted");
const crypto = require("node:crypto");

const DB_PATH = "/home/node/.n8n/database.sqlite";
const db = new sqlite3.Database(DB_PATH, sqlite3.OPEN_READONLY);

const get = (sql, params = []) => new Promise((resolve, reject) => {
  db.get(sql, params, (error, row) => error ? reject(error) : resolve(row));
});

const all = (sql, params = []) => new Promise((resolve, reject) => {
  db.all(sql, params, (error, rows) => error ? reject(error) : resolve(rows));
});

function redact(value) {
  if (typeof value !== "string") return value;
  return value
    .replace(/(api[_ -]?key|authorization|cookie|password|session[_ -]?token)\s*[:=]\s*[^\s,;]+/gi, "$1=[REDACTED]")
    .replace(/(credential(?:s)?(?:\s+with)?(?:\s+(?:id|name))?\s*[:=]?\s*)["']?[A-Za-z0-9_-]+/gi, "$1[REDACTED]")
    .replace(/Bearer\s+[A-Za-z0-9._~+\/-]+=*/gi, "Bearer [REDACTED]");
}

const OMITTED_KEYS = new Set([
  "apiKey",
  "api_key",
  "authorization",
  "cookie",
  "credential",
  "credentials",
  "password",
  "resumeUrl",
  "resume_url",
  "review_html",
  "session_token",
  "wait_resume_url",
  "webhookUrl",
  "webhook_url"
]);

function sanitizeValue(value) {
  if (typeof value === "string") return redact(value);
  if (Array.isArray(value)) return value.map(sanitizeValue);
  if (value === null || typeof value !== "object") return value;
  const clean = {};
  for (const [key, child] of Object.entries(value)) {
    if (OMITTED_KEYS.has(key)) continue;
    clean[key] = sanitizeValue(child);
  }
  return clean;
}

function canonical(value) {
  if (Array.isArray(value)) return value.map(canonical);
  if (value === null || typeof value !== "object") return value;
  return Object.fromEntries(
    Object.keys(value).sort().map((key) => [key, canonical(value[key])])
  );
}

function firstJson(data, connectionType) {
  const groups = data?.[connectionType];
  if (!Array.isArray(groups)) return null;
  for (const group of groups) {
    if (!Array.isArray(group)) continue;
    for (const item of group) {
      if (item && typeof item.json === "object") return item.json;
    }
  }
  return null;
}

function lastRun(runData, nodeName) {
  const runs = runData[nodeName];
  return Array.isArray(runs) && runs.length ? runs[runs.length - 1] : null;
}

function nodeMainJson(runData, nodeName) {
  return sanitizeValue(firstJson(lastRun(runData, nodeName)?.data, "main"));
}

function summarizeModels(runData) {
  const runs = runData["Google Gemini Chat Model"] || [];
  const generations = [];
  let promptTokens = 0;
  let completionTokens = 0;
  let totalTokens = 0;
  let usageAvailable = true;

  for (const run of runs) {
    const item = firstJson(run?.data, "ai_languageModel");
    const usage = item?.tokenUsage;
    if (!usage || ![usage.promptTokens, usage.completionTokens, usage.totalTokens].every(Number.isFinite)) {
      usageAvailable = false;
    } else {
      promptTokens += usage.promptTokens;
      completionTokens += usage.completionTokens;
      totalTokens += usage.totalTokens;
    }
    const text = item?.response?.generations?.[0]?.[0]?.text;
    if (typeof text === "string" && text.length) generations.push(text);
  }

  return {
    call_count: runs.length,
    prompt_tokens: usageAvailable ? promptTokens : null,
    completion_tokens: usageAvailable ? completionTokens : null,
    total_tokens: usageAvailable ? totalTokens : null,
    token_usage_status: runs.length === 0 ? "not_applicable" : usageAvailable ? "available" : "not_available",
    generation_texts: generations,
    cost_status: "not_available"
  };
}

function summarizeTool(runData, nodeName) {
  const runs = runData[nodeName] || [];
  const outputs = [];
  for (const run of runs) {
    const item = firstJson(run?.data, "ai_tool");
    if (!item) continue;
    if (typeof item.response === "string") {
      try {
        outputs.push(JSON.parse(item.response));
      } catch {
        outputs.push({ response: redact(item.response) });
      }
    } else {
      outputs.push(item);
    }
  }
  return { call_count: runs.length, outputs };
}

function summarizeMemory(runData) {
  const runs = runData["Obid Two-Interaction Memory"] || [];
  let history = null;
  for (const run of runs) {
    const item = firstJson(run?.data, "ai_memory");
    if (Array.isArray(item?.chatHistory)) history = item.chatHistory;
  }
  if (!history) {
    return {
      applicable: runs.length > 0,
      memory_node_run_count: runs.length,
      saved_message_count: null,
      remembered_completed_interactions_before_current: null,
      remembered_input_timestamps_before_current: []
    };
  }

  const humanEvents = [];
  for (const message of history) {
    const id = message?.id;
    const isHuman = Array.isArray(id) && id[id.length - 1] === "HumanMessage";
    const content = message?.kwargs?.content;
    if (!isHuman || typeof content !== "string") continue;
    try {
      const parsed = JSON.parse(content);
      humanEvents.push({ timestamp: parsed.timestamp ?? null, value: parsed.value ?? null });
    } catch {
      humanEvents.push({ timestamp: null, value: null });
    }
  }
  const beforeCurrent = humanEvents.slice(0, -1);
  return {
    applicable: true,
    memory_node_run_count: runs.length,
    saved_message_count: history.length,
    remembered_completed_interactions_before_current: beforeCurrent.length,
    remembered_input_timestamps_before_current: beforeCurrent.map((event) => event.timestamp)
  };
}

function safeError(error) {
  if (!error) return null;
  return {
    name: redact(error.name ?? null),
    message: redact(error.message ?? null),
    description: redact(error.description ?? null),
    node_name: redact(error.node?.name ?? null)
  };
}

async function workflowIdentity(workflowId) {
  const row = await get(
    "SELECT id, name, active, nodes, connections, settings FROM workflow_entity WHERE id = ?",
    [workflowId]
  );
  if (!row) throw new Error(`workflow ${workflowId} not found`);
  const rawNodes = JSON.parse(row.nodes);
  const nodes = rawNodes.map((node) => ({
    id: node.id,
    name: node.name,
    type: node.type,
    typeVersion: node.typeVersion,
    parameters: node.parameters,
    position: node.position,
    disabled: node.disabled ?? false
  }));
  const projection = canonical({
    id: row.id,
    name: row.name,
    nodes,
    connections: JSON.parse(row.connections),
    settings: JSON.parse(row.settings || "{}")
  });
  const serialized = JSON.stringify(projection);
  return {
    workflow_id: row.id,
    workflow_name: row.name,
    active: Boolean(row.active),
    semantic_sha256: crypto.createHash("sha256").update(serialized, "utf8").digest("hex"),
    node_count: nodes.length,
    credential_attachment_count: rawNodes.filter((node) => node.credentials && Object.keys(node.credentials).length > 0).length
  };
}

async function webhookRegistrations(workflowId) {
  const rows = await all(
    "SELECT workflowId, webhookPath, method, node FROM webhook_entity WHERE workflowId = ? ORDER BY webhookPath, method",
    [workflowId]
  );
  return rows.map((row) => ({
    workflow_id: row.workflowId,
    webhook_path: row.webhookPath,
    method: row.method,
    node_name: row.node
  }));
}

async function childExecutions(parentExecutionId) {
  const rows = await all(
    "SELECT e.id, e.workflowId, e.status, e.startedAt, e.stoppedAt, d.data " +
    "FROM execution_entity e JOIN execution_data d ON d.executionId = e.id " +
    "WHERE e.id > ? ORDER BY e.id",
    [Number(parentExecutionId)]
  );
  const childrenByParent = new Map();
  for (const row of rows) {
    let parsed;
    try {
      parsed = parseFlatted(row.data);
    } catch {
      continue;
    }
    const parent = parsed?.executionData?.runtimeData?.parentExecutionId;
    if (parent === undefined || parent === null) continue;
    const key = String(parent);
    if (!childrenByParent.has(key)) childrenByParent.set(key, []);
    childrenByParent.get(key).push({
      execution_id: Number(row.id),
      workflow_id: row.workflowId,
      status: row.status,
      started_at: row.startedAt,
      stopped_at: row.stoppedAt
    });
  }
  const result = [];
  const queue = [String(parentExecutionId)];
  const seen = new Set(queue);
  while (queue.length) {
    const parent = queue.shift();
    for (const child of childrenByParent.get(parent) || []) {
      result.push(child);
      const key = String(child.execution_id);
      if (!seen.has(key)) {
        seen.add(key);
        queue.push(key);
      }
    }
  }
  return result;
}

async function extract(executionId) {
  const entity = await get(
    "SELECT id, workflowId, status, mode, startedAt, stoppedAt, waitTill, finished " +
    "FROM execution_entity WHERE id = ?",
    [Number(executionId)]
  );
  if (!entity) throw new Error(`execution ${executionId} not found`);
  const dataRow = await get("SELECT data FROM execution_data WHERE executionId = ?", [Number(executionId)]);
  if (!dataRow) throw new Error(`execution data ${executionId} not found`);
  const parsed = parseFlatted(dataRow.data);
  const runData = parsed?.resultData?.runData || {};

  const runTimes = [];
  const nodeCounts = {};
  const nodeStatuses = {};
  for (const [nodeName, runs] of Object.entries(runData)) {
    nodeCounts[nodeName] = Array.isArray(runs) ? runs.length : 0;
    nodeStatuses[nodeName] = (runs || []).map((run) => run?.executionStatus ?? null);
    for (const run of runs || []) {
      if (!Number.isFinite(run?.startTime)) continue;
      const executionTime = Number.isFinite(run.executionTime) ? run.executionTime : 0;
      runTimes.push({ start: run.startTime, finish: run.startTime + executionTime });
    }
  }
  const runStartedMs = runTimes.length ? Math.min(...runTimes.map((time) => time.start)) : null;
  const runFinishedMs = runTimes.length ? Math.max(...runTimes.map((time) => time.finish)) : null;

  const allowlistedNodes = [
    "Minimal LLM decision",
    "Parse structured action",
    "Unrouted non-contract action",
    "Obid AI Agent",
    "Parse final decision envelope",
    "Reject malformed input",
    "Internal no-action terminal",
    "Execute runtime safety",
    "Execute Step 9 runtime safety",
    "Blocked integrated terminal",
    "Blocked before HITL terminal",
    "Prepare HITL request",
    "Finalize human decision",
    "Denied or invalid HITL terminal",
    "Validated fan on terminal",
    "Validated fan off terminal",
    "Approved fan on terminal",
    "Approved fan off terminal",
    "Direct fan on terminal",
    "Direct fan off terminal",
    "POST middleware fan on",
    "POST middleware fan off",
    "POST validated fan on",
    "POST validated fan off",
    "POST approved fan on",
    "POST approved fan off",
    "POST direct fan on",
    "POST direct fan off"
  ];
  const nodeOutputs = {};
  for (const nodeName of allowlistedNodes) {
    if (!runData[nodeName]) continue;
    nodeOutputs[nodeName] = {
      run_count: runData[nodeName].length,
      json: nodeMainJson(runData, nodeName)
    };
  }

  return {
    execution_id: Number(entity.id),
    workflow_id: entity.workflowId,
    status: entity.status,
    mode: entity.mode,
    entity_started_at: entity.startedAt,
    entity_stopped_at: entity.stoppedAt,
    wait_till: entity.waitTill,
    finished: Boolean(entity.finished),
    run_started_ms: runStartedMs,
    run_finished_ms: runFinishedMs,
    duration_ms: runStartedMs !== null && runFinishedMs !== null ? runFinishedMs - runStartedMs : null,
    last_node_executed: parsed?.resultData?.lastNodeExecuted ?? null,
    node_counts: nodeCounts,
    node_statuses: nodeStatuses,
    node_outputs: nodeOutputs,
    model: summarizeModels(runData),
    tools: {
      temperature_threshold_tool: summarizeTool(runData, "temperature_threshold_tool"),
      fan_status_tool: summarizeTool(runData, "fan_status_tool")
    },
    memory: summarizeMemory(runData),
    error: safeError(parsed?.resultData?.error),
    child_executions: await childExecutions(entity.id)
  };
}

async function main() {
  const command = process.argv[2];
  if (command === "max") {
    const workflowId = process.argv[3];
    const row = await get("SELECT MAX(id) AS maxId FROM execution_entity WHERE workflowId = ?", [workflowId]);
    console.log(JSON.stringify({ max_execution_id: row?.maxId === null ? 0 : Number(row.maxId) }));
    return;
  }
  if (command === "after") {
    const workflowId = process.argv[3];
    const minimum = Number(process.argv[4]);
    const row = await get(
      "SELECT id, workflowId, status, startedAt, stoppedAt, waitTill FROM execution_entity " +
      "WHERE workflowId = ? AND id > ? ORDER BY id LIMIT 1",
      [workflowId, minimum]
    );
    console.log(JSON.stringify(row ? {
      execution_id: Number(row.id),
      workflow_id: row.workflowId,
      status: row.status,
      started_at: row.startedAt,
      stopped_at: row.stoppedAt,
      wait_till: row.waitTill
    } : null));
    return;
  }
  if (command === "status") {
    const executionId = Number(process.argv[3]);
    const row = await get(
      "SELECT id, workflowId, status, startedAt, stoppedAt, waitTill, finished FROM execution_entity WHERE id = ?",
      [executionId]
    );
    console.log(JSON.stringify(row ? {
      execution_id: Number(row.id),
      workflow_id: row.workflowId,
      status: row.status,
      started_at: row.startedAt,
      stopped_at: row.stoppedAt,
      wait_till: row.waitTill,
      finished: Boolean(row.finished)
    } : null));
    return;
  }
  if (command === "extract") {
    console.log(JSON.stringify(await extract(Number(process.argv[3]))));
    return;
  }
  if (command === "workflow") {
    console.log(JSON.stringify(await workflowIdentity(process.argv[3])));
    return;
  }
  if (command === "webhooks") {
    console.log(JSON.stringify(await webhookRegistrations(process.argv[3])));
    return;
  }
  throw new Error(`unknown command: ${command}`);
}

main()
  .catch((error) => {
    console.error(redact(error?.stack || error?.message || String(error)));
    process.exitCode = 1;
  })
  .finally(() => db.close());
