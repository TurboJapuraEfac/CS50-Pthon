import csv

from cs50 import get_string

file = open("phonebook.csv", "a")

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()

#We can use the with keyword, which will close the file for us after we’re finished:
'''

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((name, number))

'''
