#!/usr/bin/python3
def read_file(filename=""):
    """Print the content of a UTF-8 text file."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
