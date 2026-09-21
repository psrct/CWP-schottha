#!/usr/bin/python3
n = int(input("Enter a number less than 25\n"))
if n <= 25:
    while n <= 25:
        print(f"Inside the loop, my variable is {n}")
        n += 1
else:
    print("Error")