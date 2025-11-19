#!/usr/bin/python3
from sys import argv
total = 0
if __name__ == "__main__":
    for arg in argv[1:]:
        total = total + int(arg)
print(total)
