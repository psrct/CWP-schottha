#!/usr/bin/python3
import sys

def downcase_it(s):
    return s.lower()
    
if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))