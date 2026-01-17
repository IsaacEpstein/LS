"""
PY101-PY109_small_problems

Easy1
5 Tip Calculator
Create a simple tip calculator. The program should prompt for a bill amount 
and a tip rate. The program must compute the tip, then print both the tip 
and the total amount of the bill. You can ignore input validation 
and assume that the user will enter valid numbers.

PEDAC
P:
input from user: bill amount, tip rate (assume enter valid numbers)
requirement: calculate the tip
output: print tip and bill total

E:
What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00

D: 
bill: float 
tip percentage: integer 
tip: float and keep to two decimals
total: float and kept to two decimals when printing

A:
Save the bill amount when asking, "what is the bill?" 
Save the percent amount when asking, "What is the tip percentage?" 
and get a number
Print the bill amount * the percentage amount
Print the bill amount * (1 + the percentage amount)

C:
"""
bill = float(input("What is the bill? "))
percentage = int(input("What is the tip percentage? "))
print(f"The tip amount is ${bill * (percentage / 100):.2f}")
print(f"The total bill is ${bill * (1 + (percentage / 100)):.2f}")