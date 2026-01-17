"""
PY101-PY109_small_problems

Easy2
3 Multiplying Two Numbers
Create a function that takes two arguments, multiplies them together, 
and returns the result.

PEDAC
P:
input: two arguments
requirement: multiple the values of the arguments togeter
return the product

E:
print(multiply(5, 3) == 15)  # True

D:
input: integer or float
output: integer or float

A:
create a function with two arguments
return the product of those two arguments

C:
"""
def multiply(a, b):
    return a * b

print(multiply(5, 3) == 15)  # True
