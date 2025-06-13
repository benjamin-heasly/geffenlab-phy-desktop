from pathlib import Path
from shutil import copy
import os
import sys
import time

from phy.apps.template import template_gui


# Parse the command line.
# If this grows complicated, use argparse: https://docs.python.org/3/library/argparse.html
if len(sys.argv) < 2:
    print("Usage: python run-phy.py path/to/params.py [path/for/results]")
    exit(1)

params_py = sys.argv[1]

if len(sys.argv) < 3:
    destination = "/results"
else:
    destination = sys.argv[2]

# Note the starting time, so we can find files that changed during curation.
start_time = time.time()

# Disable Chromium "sandboxing" to allow running Phy as root.
# Currently root is the only user configured for Code Ocean Ubuntu workstation.
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"

# Get the Phy params.py path from the command line.
print(f"Running Phy with {params_py}")
template_gui(params_py)

# Look for files that changed during Phy execution.
phy_dir = Path(params_py).parent
changed_files = [f for f in phy_dir.iterdir() if f.is_file() and f.stat().st_mtime > start_time]
print(f"Found {len(changed_files)} changed files.")

# Copy changed files to the Code Ocean "results" dir (or dir from command line).
for f in changed_files:
    print(f"  Copying {f} to {destination}")
    copy(f, destination)
