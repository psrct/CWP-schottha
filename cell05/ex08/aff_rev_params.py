#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    listrev = []
    for i in range(1, len(sys.argv)):
        listrev.append(sys.argv[i])
    listrev.reverse()
    print(" ".join(listrev))