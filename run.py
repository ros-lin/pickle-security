import subprocess
import os


root = os.getcwd()

commands = [
    "docker build -t pkl-inspection .",
    "docker container run --name inspect-pkl --mount type=bind,source={}/container,target=/app pkl-inspection".format(root),
    "docker rm inspect-pkl",
    "docker rmi pkl-inspection"
]

for command in commands:
    subprocess.run(command)

print("commands executed")
