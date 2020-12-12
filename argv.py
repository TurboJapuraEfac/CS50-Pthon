from sys import argv

#Argument vectors

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")

'''
(helpme) E:\CS50\Wzor>python argv.py Buddhika Weerasinghe
hello, world

(helpme) E:\CS50\Wzor>python argv.py Buddhika            
hello, Buddhika

'''
#################################################################################################################

#Python iterate over the list 

for arg in argv:
    print(arg)

'''
argv.py
Buddhika
Weerasinghe
'''


