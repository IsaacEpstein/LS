"""
PY101-PY109_small_problems
How big is the room?
Build a program that asks the user to enter the length and width of a room, 
in meters, then prints the room's area in both square meters and square feet.
Note: 1 square meter == 10.7639 square feet

PEDAC
P:
Input: from the user, length, width of a room all in meters
Output: Print the area of the room, in m2 and ft2.

E:
L = 2m
W = 4m
A (m2) = 8m2
A (ft2) = 2m x 4m * 10.7639ft2/m2

D:
Input: str --> float
Output: string + float

A:
The program asks the user to enter the length of a room in meters.
The program asks the user to enter the width of a room in meters.
When the program asks, the program needs to check to make sure the input
is a number greater than 0.
If the input is a number greater than 0, then the program will continue. 
If the number is not a number and the value is not greater than 0,
the program will tell the user to enter a number greater than 0 and prompt
them again to input.
The program prints both the area in m2 and ft2.

C:
"""

# # def check_float(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             if value > 0:
#                 return value
#             else:
#                 print('Please input a positive number.')
#         except ValueError:
#             print('Invalid entry. Please input a positive number.')

# length_meters = check_float('Please send the length of a room in meters: ')
# width_meters = check_float(f'Please send the width of a room in meters: ')
# print(f'The area of the room is {length_meters * width_meters} square meters '
#       f'and {length_meters * width_meters * 10.7639:.1f} square feet.')


def check_m_f(answer):
    while True:
        choice = input(answer).strip().lower()
        if choice == 'meters' or choice == 'feet':
            return choice
        else:
            print("Please enter either of the words meters or feet.")

def check_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid entry. Please enter a positive number.")

unit = check_m_f("Use meters or feet to measure the room? ")
length = check_float(f'Please write the length of a room in {unit}: ')
width = check_float(f'Please write the width of a room in {unit}: ')
print(f'The area of the room is {length * width} square {unit}.')