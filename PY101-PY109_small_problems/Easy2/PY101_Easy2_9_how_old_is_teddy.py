# Your code goes here
"""
PY101-PY109_small_problems

Easy2
9 How Old is Teddy?
Build a program that randomly generates and prints Teddy's age. To get the 
age, you should generate a random number between 20 and 100, inclusive.

PEDAC
P:
input: random generator
output: prints Teddy's age
requirements: can pick a random from 20 to 100, inclusive

E:
Teddy is 69 years old!

D:
input: random integer
output: string with that randome integer

A:
generate random number from 20 to 100
print out statement with Teddy's age

C:
"""
# import random
# print(f'Teddy is {random.randint(20,100)} years old.')

# Further Exploration
# Modify this program to ask for a name, then print the age for that person. 
# For an extra challenge, use "Teddy" as the name if no name is entered.

import random

name = input('What is your name? ')
if name == '':
    name = 'Teddy'
print(f'{name} is {random.randint(20,100)} years old.')
