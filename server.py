#!/usr/bin/env python3
"""Local static preview server for the GoodEats promotional landing page."""
from __future__ import annotations

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from build_static import PUBLIC, build

PORT = int(os.environ.get("PORT", "4173"))


class StaticHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".woff2": "font/woff2",
    }


if __name__ == "__main__":
    build()
    handler = partial(StaticHandler, directory=str(PUBLIC))
    server = ThreadingHTTPServer(("0.0.0.0", PORT), handler)
    print(f"GoodEats static preview listening on 0.0.0.0:{PORT}; no order or request API is running.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
