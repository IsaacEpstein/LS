"""
PY101-PY109_small_problems

Easy2
7 Exclusive Or
The or operator returns a truthy value if either or both of its operands 
are truthy, a falsy value if both operands are falsy. The and operator 
returns a truthy value if both of its operands are truthy, and a falsy 
value if either operand is falsy. This works great until you need only 
one of two conditions to be truthy, the so-called exclusive or, also 
known as xor (pronounced "ECKS-or").

In this exercise, you will write an xor function that takes two arguments, 
and returns True if exactly one of its arguments is truthy, False otherwise.



PEDAC
P:
write a function
input: two arguments
output: true if exactly one is truthy and false otherwise

E:
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

D:
input: anything
output: bool

A:
initiate a function which takes two arguments
if one is true and one is false, return true
otherwise return false

C:
"""
def xor(a, b):
    # if bool(a) and not bool(b):
    #     return True
    # elif bool(b) and not bool(a):
    #     return True
    # else:
    #     return False
    return bool(a) != bool(b)
    # return bool(a) ^ bool(b)


print(xor(5, 0))
print(xor(False, True))
print(xor(1, 1))
print(xor(True, True))