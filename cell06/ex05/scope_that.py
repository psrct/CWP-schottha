#!/usr/bin/python3

def add_one(num):
    num += 1
    print(f"Number inside add_one: {num}")

numx = 42
print(f"Number before add_one: {numx}")

add_one(numx)

print(f"Number after add_one: {numx}")
