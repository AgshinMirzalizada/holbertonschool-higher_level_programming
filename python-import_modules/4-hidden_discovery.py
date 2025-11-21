#!/usr/bin/python3
import hidden_4
if _name_ == "_main_":
    names = dir(hidden_4)
    for name in names:
        if not name.startswith(""):
            print(name)
