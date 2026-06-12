#!/usr/bin/env python3
"""Shim: the canonical checker now ships inside the skill (plan B, 2026-06-12)
at skills/dashmotion/scripts/check_diagram.py so generation-time Step 6 can
run it mechanically. This wrapper keeps every documented eval/test command
working unchanged. Single source of truth lives in the skill copy.

Usage: python3 eval/check_diagram.py file1.html [file2.html ...] [--json]
"""

import os
import runpy
import sys

CANONICAL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "skills", "dashmotion", "scripts",
                         "check_diagram.py")

if not os.path.exists(CANONICAL):
    sys.exit(f"canonical checker not found: {CANONICAL}")

sys.argv[0] = CANONICAL
runpy.run_path(CANONICAL, run_name="__main__")
