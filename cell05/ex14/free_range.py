#!/usr/bin/python3
import sys

if len(sys.argv) <= 2:
    print("none")
else:
    array = []
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    while True:
        if num1 == num2:
            array.append(num1)
            break
        else:
            array.append(num1)
            num1 += 1
    print(array)