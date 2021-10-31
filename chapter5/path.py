import os

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, "file/bankbalance.txt")

# file = os.path.expanduser("~/comprog/chapter5/file/bankbalance.txt")

print(dirname)

with open(file, "r") as f:
    for line in f:
        print(line.strip())

