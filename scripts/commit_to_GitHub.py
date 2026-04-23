import subprocess

#Pushing changes to master branch
BRANCH = "master"
commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", "removed useless lines"],
    ["git", "push", "-u", "origin", BRANCH]
]

for cmd in commands:
    subprocess.run(cmd)