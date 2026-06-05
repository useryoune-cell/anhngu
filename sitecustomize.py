# -*- coding: utf-8 -*-
"""Keep Python console output UTF-8 friendly on Windows terminals."""

import sys


for stream_name in ("stdout", "stderr"):
    stream = getattr(sys, stream_name, None)
    if stream and hasattr(stream, "reconfigure"):
        try:
            stream.reconfigure(encoding="utf-8")
        except (LookupError, ValueError):
            pass
