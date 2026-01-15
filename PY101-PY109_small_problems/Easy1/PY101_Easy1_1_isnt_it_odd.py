"""
PY101-PY109_small_problems

Easy1
1 Isn't it Odd?
Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

PEDAC
P:
Requirement: Write a function
input: integer argument
Output: return True
Condition: 
True when integer argument absolute value is odd
False otherwise

E:
abs(5) = 5
abs(-5) = 5
abs(0) = 0

D:
Integer

A:
An integer gets put into a function.  
Only if the integer is less than 0, then mulitply the number by -1. 
If by dividing by 2 has a remainder, it's odd and the function should return True.
Otherwise, it should return False.

C:
"""
def abs_value(number):
    if number < 0:
        number = number * -1
    if number % 2 != 0:
        return True
    else:
        return False

print(abs_value(-5))
print(abs_value(-6))
print(abs_value(0))
print(abs_value(5))
print(abs_value(6))

# def is_odd(number):
#     return abs(number) % 2 == 1

# print(is_odd(-5))
# print(is_odd(-6))
# print(is_odd(0))
# print(is_odd(5))
# print(is_odd(6))