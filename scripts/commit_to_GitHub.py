import subprocess

#Pushing changes to master/main branch
BRANCH = "main"

message = input("Commit message: ")
commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", message],
    ["git", "push", "-u", "origin", BRANCH]
]

if __name__ == '__main__':
    print('Pushing to GitHub')
    for cmd in commands:
        subprocess.run(cmd, check=True)

    print("Push completed.")
