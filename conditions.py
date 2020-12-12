from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

'''
We can import entire libraries, and use functions inside them as if they were a struct:
import cs50

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")

'''


if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
