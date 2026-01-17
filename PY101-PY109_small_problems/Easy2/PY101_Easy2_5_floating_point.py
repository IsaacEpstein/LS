"""
PY101-PY109_small_problems

Easy2
5 Floating Point Arithmetic
Write a program that prompts the user for 
two positive numbers (floating-point), 
then prints the results of the following operations on those two numbers: 
addition, subtraction, product, quotient, floor quotient, remainder, and 
power. Do not worry about validating the input.

PEDAC
P:
input: two floats
output: addition, subtraction, product, quotient, floor quotient, remainder, 
and power of the two floats
requirement: prompt the user for the floats, print resutls

E:
==> Enter the first number:
3.141592
==> Enter the second number:
2.718282
==> 3.141592 + 2.718282 = 5.859874
==> 3.141592 - 2.718282 = 0.4233100000000003
==> 3.141592 * 2.718282 = 8.539732984944001
==> 3.141592 / 2.718282 = 1.1557270364149121
==> 3.141592 // 2.718282 = 1.0
==> 3.141592 % 2.718282 = 0.4233100000000003
==> 3.141592 ** 2.718282 = 22.45914942746313

D:
input: float
output: float

A:
ask the user for the first float.  get the float
ask the user for the second float. get the float
print the results of 
addition
subtraction
product
quotient
floor quotient
remainder
power

C:
"""
a = float(input(f'What is the first number? '))
b = float(input(f'What is the second number? '))
print(f'===> {a} + {b} = {a+b}')
print(f'===> {a} - {b} = {a-b}')
print(f'===> {a} * {b} = {a*b}')
print(f'===> {a} / {b} = {a/b}')
print(f'===> {a} // {b} = {a//b}')
print(f'===> {a} % {b} = {a%b}')
print(f'===> {a}**{b} = {a**b}')