#!/usr/bin/python3
total=0
from sys import argv
if __name__ == "__main__":
    for arg in argv[1:]:
        total = total + int(arg)
print(total)
