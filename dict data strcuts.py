from cs50 import get_string

people = {
    "Brian": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")

if name in people:
    number = people[name] #Search is auto handled using hash tables in built
    print(f"Number: {number}")

