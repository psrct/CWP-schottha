#!/usr/bin/python3

def array_of_names(dict):
    list = []
    for x,y in dict.items():
        list.append(f"{x.capitalize()} {y.capitalize()}")
    return list

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))