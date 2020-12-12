from cs50 import get_string


#Upprecase
s = get_string("Before:  ")
print("After: ", end="")
for c in s: #iterate over characters using for loop
    print(c.upper(), end="")
print()


