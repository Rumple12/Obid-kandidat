# Projektplan - Agentic Design Patterns \& Tillförlitlighet för IoT-styrning







> \[!IMPORTANT]

> This file is a source summary of the original Obid thesis plan.

> In the new-yacoub thesis mode, it is reference material only.

> It is NOT the active implementation scope.

> The active implementation scope is defined in:

> - docs/plans/implementation-plan.md

> - docs/ongoing/yacoub-scope.md

> - docs/ongoing/obid-minimum-integration.md







**Student:** Obid Alrhman Aljabi

## 1\. Bakgrund och problembeskrivning

Large Language Models (LLMs) är i grunden icke-deterministiska, vilket innebär att de kan producera olika utfall för samma input. Enligt Huang et al. \[1] leder detta till fenomenet hallucinationer, vilket utgör en betydande säkerhetsrisk när modellen appliceras på Agentic AI \[2] - system där modellen ges verktyg för att styra fysiska IoT-enheter.

En hallucinerande chattbot är irriterande; en hallucinerande IoT-agent som stänger av en kylfläkt för att den trodde att servern var kall är farlig. Problemet ligger i att designa en mjukvaruarkitektur som begränsar LLM-beteende och säkerställer tillförlitlig verktygsanvändning utan att offra flexibiliteten i den naturliga språkförståelsen \[3].

## 2\. Syfte och mål

Syftet med detta examensarbete är att designa, implementera och utvärdera ett tillförlitligt Agentic Workflow i n8n som autonomt kan hantera IoT-enheter med en mätbar framgångsgrad.

Mitt specifika mål är att utveckla den kognitiva arkitekturen, logiken, minneshanteringen och säkerhetsspärrarna som tillåter en AI att fatta korrekta beslut baserat på sensordata från hårdvarulagret \[4].

## 3\. Omfattning och ansvarsområden

Mitt arbete fokuserar på systemets hjärna och är uppdelat i tre mjukvarutekniska pelare:

### A. Agentarkitektur (Graf/Flöde)

* **Uppgift:** Konfiguration av "AI Agent Node" och verktygsdefinitioner i n8n.
* **Design:** Implementering av "ReAct", en metodik för att låta LLMs resonera och agera i synergi \[5]. Detta skapar slutna loopar där agenten observerar data, tänker, agerar och observerar igen.
* **Tekniskt arbete:** Skapande av JSON-scheman som definierar hur agenten kommunicerar med Jakobs hårdvaru-API.

### B. Kognitiv design (Prompts \& Minne)

* **Uppgift:** Ingenjörsmässig utformning av logiken för att maximera intelligens inom ett begränsat kontextfönster.
* **Leverans: System Prompts:** Skrivande av strikta beteendeinstruktioner för att styra agentens persona och beslutsfattande.
* **Minneshantering:** Implementering av Window Buffer Memory för att säkerställa att agenten minns tidigare handlingar utan att överträda hårdvarans resursbegränsningar.

### C. Säkerhetslagret

* **Uppgift:** Förhindra Ghost Actions och farliga kommandon.
* **Leverans: Human-in-the-Loop:** Design av noder som interceptar högrisk-kommandon för manuellt godkännande \[6].
* **Output Parsing:** Validering av agentens output t.ex. via regex för att säkerställa korrekt syntax innan data skickas till hårdvaran.

## 4\. Samarbete och gränsdragning

Detta projekt genomförs i samarbete med Jakob \[Efternamn]. Medan Jakob ansvarar för den fysiska infrastrukturen (Raspberry Pi, Docker-optimering och sensor-API), ansvarar jag för den logiska orkestreringen. Integrationen sker via ett gemensamt definierat API-gränssnitt.

## 5\. Tidsplan

Total arbetsbelastning beräknas till 350 timmar.

* **April:** Utforma det kognitiva arbetsflödet i n8n: konfigurering av AI Agent, verktygsdefinitioner samt gemensamt JSON-schema för kommunikationen med Yacoubs hårdvaru-API. Ta fram systemprompts och den övergripande beslutslogiken.
* **Maj:** Implementera agentens kärnbeteende: promptstruktur, begränsat minne samt resonemangs- och handlingsflöde för IoT-styrning. Bygga säkerhetslagret med output parsing och validering för att säkerställa korrekt kommandostruktur.
* **Juni:** Slutföra tillförlitlighetslagret genom integration och testning: koppla arbetsflödet till det fysiska API-gränssnittet, införa Human-in-the-Loop för högriskkommandon och utvärdera hur säkert och korrekt agenten hanterar IoT-beslut.

## Referenser

\[1] Y. Huang et al., "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions," arXiv preprint arXiv:2311.05232, 2023. https://arxiv.org/abs/2311.05232

\[2] R. Sapkota, K. I. Roumeliotis, och M. Karkee, "AI agents vs. agentic AI: A conceptual taxonomy, applications and challenges," arXiv preprint arXiv:2505.10468, maj 2025. https://www.sciencedirect.com/science/article/pii/S1566253525006712

\[3] S. Hosseini och H. Seilani, "The role of agentic AI in shaping a smart future: A systematic review," Array, vol. (pending), Art. no. 100399, maj 2025. https://www.sciencedirect.com/science/article/pii/S2590005625000268

\[4] S. Greengard, The Internet of Things, uppdaterad uppl. Cambridge, MA, USA: MIT Press, 2021. https://books-library.website/files/books-library.net-10072224Wp1Q5.pdf

\[5] S. Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," arXiv preprint arXiv:2210.03629, 2023. https://arxiv.org/abs/2210.03629

\[6] OpenAI, "Governance of Superintelligence," openai.com, 2023. \[Online]. Tillgänglig: https://openai.com/blog/governance-of-superintelligence.

