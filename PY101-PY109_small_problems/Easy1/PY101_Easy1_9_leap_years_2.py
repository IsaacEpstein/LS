# Your code goes here
"""
PY101-PY109_small_problems

Easy1
9 Leap Years (Part 2)
In the previous exercise, we assumed that the Gregorian calendar has been in 
continuous use since the year 1. However, the Gregorian calendar wasn't 
adopted until much later; prior to that, much of the world used the Julian 
calendar, which observed leap year every 4 years.

in 1752, England, Ireland, and the British colonies all switched to the 
Gregorian calendar. Update the function from the previous exercise so it 
uses the Julian calendar prior to 1752, and the Gregorian calendar 
starting in 1752.

PEDAC
P:
input: number/year (greater than 0)
output: True or False (T for leap year, F for not leap year)
requirements: 
Before 1752 use Julian
leap year is every 4 years

After 1752, use Gregorian calendar
year / 400 no remainder = leap year
year / 100 and not year / 400, not a leap year
year / 4 and not year / 100, it is a leap year
all else is not leap year

E:
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

D: 
input: integer
output: bool

A:
A function takes a number. 
That number has to be greater than 0.  If not, then break and print out
that the number has to be greater than 0.

To determine if it's leap year,
if the year is less than 1752,
if the year is divisible by 4, then it's a leap year

if the year is 1752 or greater,
if the year is divisible by 400, then it's a leap year.
if the year is divisible by 100 but NOT 400, not a leap year.
if the year is divisible by 4 and not divisible by 100, it IS a leap year.
if it's a leap year, return True.  Otherwise, return False.


C:
"""
def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError('Invalid. Year must be an integer.')
    if year <= 0:
        raise ValueError('Invalid. Year must be greater than 0.')
    if year < 1752 and year % 4 == 0:
        return True
    elif year % 400 == 0:
            return True
    elif year % 100 == 0:
            return False
    else:
        return year % 4 == 0

test_cases = [1, 2, 3, 4, 100, 200, 300, 400, 1000, 1100, 1200, 
              1300, 1751, 1752, 1753, 1800, 1900, 2000, 2023, 
              2024, 2025, -1, 0, 3.14, 'abc', None]

for year in test_cases:
    try:
        print(f"{year}: {is_leap_year(year)}")
    except (TypeError, ValueError) as e:
        print(f"{year}: {e}")






# def is_leap_year(year):
#     if not isinstance(year, int) or year <= 0:
#         raise TypeError('Invalid. Please use a positive integer.')
#     match (year % 400, year % 100, year % 4):
#         case (0, _, _):
#             return True
#         case (_, 0, _):
#             return False
#         case (_, _, 0):
#             return True
#         case _:
#             return False

# test_cases = [1, 2, 3, 4, 100, 200, 300, 400, 1000, 1100, 1200, 
#               1300, 1751, 1752, 1753, 1800, 1900, 2000, 2023, 
#               2024, 2025, -1, 0, 'abc', 3.14, None]

# for year in test_cases:
#     try:
#         result = is_leap_year(year)
#         print(f'{year}: {result}')
#     except (TypeError, ValueError) as e:
#         print(f'{year}: Error - {e}')

'''
print("1 ", is_leap_year(1))
print("2 ", is_leap_year(2))
print("3" , is_leap_year(3))
print("4" , is_leap_year(4))
print("100", is_leap_year(100))
print("200", is_leap_year(200))
print("300", is_leap_year(300))
print("400", is_leap_year(400))
print("1000", is_leap_year(1000))
print("1100", is_leap_year(1100))
print("1200", is_leap_year(1200))
print("1300", is_leap_year(1300))
print("1751", is_leap_year(1751))
print("1752", is_leap_year(1752))
print("1753", is_leap_year(1753))
print("1800", is_leap_year(1800))
print("1900", is_leap_year(1900))
print("2000", is_leap_year(2000))
print("2023", is_leap_year(2023))
print("2024", is_leap_year(2024))
print("2025", is_leap_year(2025))
print("-1", is_leap_year(-1))
print("-0", is_leap_year(0))
print("abc", is_leap_year('abc'))
'''