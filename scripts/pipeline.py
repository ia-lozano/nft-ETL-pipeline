import subprocess
import sys
import time
from pathlib import Path

#Location independency
BASE = Path(__file__).parent

SCRIPTS = [
    BASE/"E_Extract.py",
    BASE/"Update_raw_file.py",
    BASE/"T_Transform.py",
    # Commented out to avoid the "hey wehere is the password?" error.
    #BASE/"L_Load.py",
    # Commented out to avoid sending potentially broken pipelines to GitHub.
    #BASE/"commit_to_GitHub.py",
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
        print(f"Ooops, something when wrong went running {script} terminating pipeline...")
        sys.exit(1)

print('Executing Pipeline...')
for script in SCRIPTS:
    run(script)

print('Pipeline finalized successfully.')