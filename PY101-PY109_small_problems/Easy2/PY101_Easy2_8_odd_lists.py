# Your code goes here
"""
PY101-PY109_small_problems

Easy2
8 Odd Lists
Write a function that returns a list that contains every other element of 
a list that is passed in as an argument. The values in the returned list 
should be those values that are in the 1st, 3rd, 5th, and so on elements 
of the argument list.

PEDAC
P:
input: list
output: list
requirement: filter through and return every other element of a list

E:
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

D:
input: list
output: list

A:
initilize a function which takes a list as an argument
step through and return every other element

C:
"""
def oddities(first_list):
    new_list = []
    # for item in range(0, len(first_list), 2):
    #     new_list.append(first_list[item])
    # return new_list
#     for item in first_list[::2]:
#         new_list.append(item)
#     return new_list
#     return first_list[::2]
    return first_list[1::2] #gets the 2,4,6th element of the list

print(oddities([2, 3, 4, 5, 6])) #[2, 4, 6])   True
print(oddities([1, 2, 3, 4])) #[1, 3])        True
print(oddities(["abc", "def"])) #['abc'])      True
print(oddities([123])) #[123])                 True
print(oddities([])) #[])                       True