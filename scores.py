'''
Lists, strings

'''
from cs50 import get_int

#Get score as a input
scoresnew = []
for i in range(3):
    scoresnew.append(get_int("Score: "))
print("Average score: " + str(sum(scoresnew) / len(scoresnew)))


scores = [72, 73, 33]

# TypeError: can only concatenate str (not "float") to str
# print("Average: " + (sum(scores) / len(scores)))

#Way 1
print("Average: " + str(sum(scores) / len(scores)))

#Way 2
print(f"Average with brackets: {sum(scores) / len(scores)}")

#Way 3

average = sum(scores) /len(scores)
print(f"Third Average:{average}")



