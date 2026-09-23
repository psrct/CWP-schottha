#!/usr/bin/python3
import sys
import re

if len(sys.argv) <= 2:
    print("none")
else:
    par1 = sys.argv[1]
    par2 = sys.argv[2]
    matches = re.findall(par1, par2)
    print(len(matches))