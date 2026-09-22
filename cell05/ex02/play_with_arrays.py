#!/usr/bin/python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
new = set(new)
for n in original:
    if n > 5:
        new.add(n + 2)

print(original)
print(set(new))