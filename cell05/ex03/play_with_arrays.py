#!/usr/bin/python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for n in original:
    if n > 5:
        new.append(n + 2)
newset = set(new)
print(original)
print(newset)