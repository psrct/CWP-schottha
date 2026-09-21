#!/usr/bin/python3
n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))
sum = n1 * n2
print(f"{n1} * {n2} = {sum}")
if sum < 0:
    print("This result is negative.")
elif sum > 0:
    print("This result is positive.")
else:
    print("This result is positive and negative.")
