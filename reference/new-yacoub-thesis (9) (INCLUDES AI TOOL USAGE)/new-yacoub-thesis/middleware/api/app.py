"""Local middleware entry point for the Step 4 skeleton."""

from __future__ import annotations

import os
from http.server import ThreadingHTTPServer

from middleware.api.routes import MiddlewareRequestHandler


def main() -> None:
    host = os.getenv("MIDDLEWARE_HOST", "127.0.0.1")
    port = int(os.getenv("MIDDLEWARE_PORT", "8000"))
    server = ThreadingHTTPServer((host, port), MiddlewareRequestHandler)

    print(f"new-yacoub middleware running at http://{host}:{port}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping middleware.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
