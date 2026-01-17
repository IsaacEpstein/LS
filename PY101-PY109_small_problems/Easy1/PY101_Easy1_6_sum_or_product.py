"""
PY101-PY109_small_problems

Easy1
6 Sum or Product of Consecutive Integers
Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of 
all numbers between 1 and the entered integer, inclusive.

PEDAC
P:
Input: user enters a number (requirement: has to be an integer > 0)
Input: user enters sum or product (requirement: has to be a string and match
either 's" or 'p')
Output: either calculate the sum or the product of all the numbers between
1 and the number

E:
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s
The sum of the integers between 1 and 5 is 15.

Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p
The product of the integers between 1 and 6 is 720.

D: 
Input: integer
Input: string
Output: integer

A:
Ask the user for a number.  Store that value as an integer.
Ask the user to choose between sum and product.
Either add up or sum all the numbers between 1 and the number (inclusive)
Print the sum or the product.

C:
"""
while True:
    try:
        number = int(input('Enter an integer greater than 0: '))
        if number > 0:
            break
        else:
            print("Invalid. Must be greater than 0.")
    except ValueError:
        print("Invalid. Must be an integer.")

sum_or_product = input('Enter "s" for sum and "p" for product: ')
while sum_or_product != 's' and sum_or_product != 'p':
    sum_or_product = input('Invalid. Enter "s" for sum and "p" for product: ')

total = 0 if sum_or_product == 's' else 1

for i in range(1, number+1):
    if sum_or_product == 's':
        total += i
    else:
        total *= i

print(f'The product of the integers between 1 and {number} is {total}.')