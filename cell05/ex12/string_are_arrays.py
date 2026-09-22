#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    count = 0
    word = sys.argv[1]
    for i in word:
        if i == "z":
            count += 1
    print(count*"z")