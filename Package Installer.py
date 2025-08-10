import os

with open("files/libraries.txt", "r") as f:
    packages = f.readlines()

for package in packages:
    os.system(f"py -m pip install {package}")