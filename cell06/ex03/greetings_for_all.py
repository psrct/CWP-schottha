#!/usr/bin/python3
def greetings(s="Hello, noble stranger"):
    if type(s) is int:
        print("Error! It was not a name.")
    else:
        print(f"Hello, {s}.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)