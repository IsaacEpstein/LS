"""
PY101-PY109_small_problems

Easy1
2 Odd Numbers
Print all odd numbers from 1 to 99, inclusive, 
with each number on a separate line.
Bonus Question: Can you solve the problem 
by iterating over just the odd numbers?

PEDAC
P:
Print
Odd numbers
Range from 1 to 99, including 1 and 99
Separate line
Iterate (only on odd numbers)
Input: none
Output: Log to terminal

E:
Not sure how to do this part

D:
Odd numbers (integers)

A:
Print starting with 1 and then add 2 to get to the next odd number, 3.
Repeat that until you print 99 and then stop.

C:
"""
# for i in range(1,100,2):
#     print(i)

start = int(input('Enter an odd start number greater than 0: '))
while start < 0 or start % 2 == 0:
    start = int(input('Enter an odd start number greater than 0: '))
end = int(input(f'Enter an odd end number greater than 0 and {start}: '))
while end < 0 or end < start or end % 2 == 0:
    end = int(input(f'Enter an odd end number greater than 0 and {start}: '))
for i in range(start, end+1, 2):
    print(i)