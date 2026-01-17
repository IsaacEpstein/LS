# Your code goes here
"""
PY101-PY109_small_problems

Easy1
10 Multiples of 3 or 5
Write a function that computes the sum of all numbers between 1 and some 
other number, inclusive, that are multiples of 3 or 5. For instance, if the 
supplied number is 20, the result 
should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.

PEDAC
P:
write a function
input: integer greater than 1
output: sum of numbers between 1 and the input, inclusive
requirement: the numbers must be multiples of 3 or 5.

E:
For instance, if the 
supplied number is 20, the result 
should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20)

D: 
input: integer
output: integer

A:
function takes an integer
make a list of numbers between 1 and the integer
filter them if they are either a mulitple of 3 or 5
return the sum of those numbers

C:
"""
def multiple_3_5(input):
    list_of_numbers = []
    sum_of_numbers = 0
    for number in range(1, input+1):
        if number % 3 == 0 or number % 5 == 0:
            list_of_numbers.append(number)
    # sum_of_numbers = sum(list_of_numbers)
    # return sum_of_numbers
    for i in list_of_numbers:
        sum_of_numbers += i
    return sum_of_numbers

print(multiple_3_5(20))
print(multiple_3_5(15))