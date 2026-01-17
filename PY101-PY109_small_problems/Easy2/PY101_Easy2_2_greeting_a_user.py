"""
PY101-PY109_small_problems

Easy2
2 Greeting a user
Write a program that asks for user's name, then greets the user. 
If the user appends a ! to their name, the computer will yell the greeting 
(print it using all uppercase).

PEDAC
P:
input: user's name (string)
output: greet the user
requirements: if the last character of the name is !, the greet should be all 
caps

E:
What is your name? Sue
Hello Sue.

What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?

D:
input: string
output: string

A:
ask the user's name and have them input it
if the user's name doesn't end in !, then greet them, 
otherwise, greet them with all caps

C:
"""
name = input(f'What is your name? ')
# if name[-1] != '!':
#     print(f'Hello, {name}, how are you?')
# else:
#     print(f'HELLO, {name.upper()}, HOW ARE YOU?')

if not name.endswith('!'):
    print(f'Hello, {name}, how are you?')
else:
    print(f'HELLO, {name.upper()}, HOW ARE YOU?')