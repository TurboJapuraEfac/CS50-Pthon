import sys

if len(sys.argv) != 2:
    print("missing command-line argument")
    sys.exit(1)
    
print(f"hello, {sys.argv[1]}")
sys.exit(0)

#Answers
'''
(helpme) E:\CS50\Wzor>python exit.py
missing command-line argument

(helpme) E:\CS50\Wzor>python exit.py Helloooooooooooooooooooooooooooooooo
hello, Helloooooooooooooooooooooooooooooooo

'''
