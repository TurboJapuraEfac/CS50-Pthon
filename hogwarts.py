import csv

#Initial count values
houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

#file name = Sorting Hat (Responses) - Form Responses 1.csv
with open("Sorting Hat (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.reader(file)
    # next skip 1st row
    next(reader)
    for row in reader:
        house = row[1]      # we ignore row[1] because it is timestamp
        houses[house] += 1  #increment house count

for house in houses:
    print(f"{house}: {houses[house]}")

