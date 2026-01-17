"""
PY101-PY109_small_problems

Easy2
12 Write a function that takes a number as an argument. If the argument 
is a positive number, return the negative of that number. If the argument 
is a negative number, return it as-is.

PEDAC
P:
input: number
output: return a negative number if the number is positive or negative
requirement: write a function and return a number

E:
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

D:
input: integer
output: integer

A:
initialize a function which takes an integer as an argument
if the number is greater than zero, multiply the number by -1 
if the number is negative, return the number

C:
"""
def negative(number):
    return -abs(number)
    # return number * -1 if number > 0 else number
    # if number > 0:
    #     number = number * -1
    #     return number
    # else:
    #     return number
    
print(negative(5)) # == -5)      # True
print(negative(-3)) # == -3)     # True
print(negative(0)) # == 0)  