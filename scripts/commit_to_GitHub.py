import subprocess

#Pushing changes to master branch
commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", "removed useless lines"],
    ["git", "push", "-u", "origin", "master"]
]

for cmd in commands:
    subprocess.run(cmd)