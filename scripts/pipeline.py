import subprocess
import sys
import time
from pathlib import Path

SCRIPTS = [
    "scripts/E_Extract.py",
    "scripts/Update_raw_file.py",
    "scripts/T_Transform.py",
    # Commented out to avoid the "hey wehere is the password?" error.
    #"scripts/L_Load.py",
    # Commented out to avoid sending potentially broken pipelines to GitHub.
    #"scripts/commit_to_GitHub.py",
]

def run(script: str):
    result=subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print(result.stderr)

    if result.returncode !=0:
        print(f"Ooops, something when wrong when running {script} terminating pipeline...")
        exit(1)

for script in SCRIPTS:
    run(script)