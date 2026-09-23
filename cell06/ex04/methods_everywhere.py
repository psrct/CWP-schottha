#!/usr/bin/python3
import sys

def shrink(s):
    return(s[:8])

def enlarge(s):
    if len(s) < 8:
        count = 8-len(s)
        print(f"{s}{count*"z"}")
    else:
        print(f"{s}")
    

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        word = shrink(sys.argv[i])
        enlarge(word)