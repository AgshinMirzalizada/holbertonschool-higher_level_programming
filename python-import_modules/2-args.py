#!/usr/bin/python3

from sys import argv
if __name__=="__main__":
    num=len(argv)-1
    if num == 0:
        print("0 arguments.")
    else:
        print(f"{num} arguments:")

for i in range(1, len(argv)):
        print(f"{num}: {argv[i]}")

