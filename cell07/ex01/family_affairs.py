#!/usr/bin/python3

def find_the_redheads(dict):
    redheads = list(filter(lambda name: dict[name] == "red", dict))
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))