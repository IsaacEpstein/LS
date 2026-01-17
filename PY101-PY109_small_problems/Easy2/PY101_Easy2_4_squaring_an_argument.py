"""
PY101-PY109_small_problems

Easy2
4 Squaring an Argument
Using the multiply function from the "Multiplying Two Numbers" exercise, 
write a function that computes the square of its argument (the square is 
the result of multiplying a number by itself).

PEDAC
P:
input: integer argument 
output: integer
requirement: write a function which will return the square of the argument

E:
print(square(5) == 25)   # True
print(square(-8) == 64)  # True

D:
input: integer
output: integer

A:
define function
pass in an integer
return the integer times itself

C:
"""
def multiply(a, b):
    return a * b

def square(a):
    # return a*a
    # return a**2
    return multiply(a, a)

def power(a, n):
    total = 1
    for _ in range(n):
        total = multiply(total, a)
    return total

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(power(2, 3))
print(power(3, 3))
print(power(2, 4))