# Your code goes here
"""
PY101-PY109_small_problems

Easy2
10 When Will I Retire?
Build a program that displays when the user will retire and how many years 
she has to work till retirement.

PEDAC
P:
input: age and retirement age
output: print the year and how many years left until retirement

E:
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!

D:
input: integer
output: string

A:
ask the age
ask the retirement age
print the year, the year they will retire and how many years they have left

C:
"""
from datetime import datetime as dt

current_year = dt.now().year
age = int(input('How old are you? '))
retirement_age = int(input('At what age would you like to retire? '))
print(f'It\'s {current_year}. You will retire in {current_year + retirement_age - age}.')
print(f'You have only {retirement_age - age} years to go.')