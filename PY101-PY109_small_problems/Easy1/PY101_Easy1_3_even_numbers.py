"""
PY101-PY109_small_problems

Easy1
3 Even Numbers
Print all even numbers from 1 to 99, inclusive, 
with each number on a separate line.
Bonus Question: Can you solve the problem by 
iterating over just the even numbers?

PEDAC
P:
print
input: none
output: even numbers between 1 and 99
All numbers must be on a separate line
Iterate just on the even numbers between 1 and 99

E:
2
4
6
...
98

D:
Input: none
Output: even numbers

A:
In a range from 1 to 99 iterate up by 2
First check if the number is greater than 0.
Check if the number is even, if not, add 1 and then continue iterating.
Print out numbers until you get to 99

C:
"""
for i in range(2,100,2):
    print(i)

