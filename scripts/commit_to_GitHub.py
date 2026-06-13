import subprocess

#Pushing changes to master/main branch
BRANCH = "main"

message = input("Commit message: ")
commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", message],
    ["git", "push", "-u", "origin", BRANCH]
]

for cmd in commands:
    subprocess.run(cmd, check=True)

print("Push completed.")
