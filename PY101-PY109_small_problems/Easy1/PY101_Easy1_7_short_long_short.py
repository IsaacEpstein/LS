# Your code goes here
"""
PY101-PY109_small_problems

Easy7
7 Short Long Short
Write a function that takes two strings as arguments, determines the length 
of the two strings, and then returns the result of concatenating the shorter 
string, the longer string, and the shorter string once again. You may assume 
that the strings are of different lengths.

PEDAC
P:
input: two strings (different lengths)
requirement: need to concatenate the strings 
output: short + long + short

E:
string1 = 'cat'
string2 = 'mouse'
output = 'catmousecat'

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

D: 
inputs: strings
output: string

A:
write a function which takes these two strings
determine which string is shorter and then concatenate the short one then the 
long one and then the short one again

C:
"""
# def short_long(str1, str2):
#     if len(str1) < len(str2):
#         concat_string = str1 + str2 + str1
#     else:
#         concat_string = str2 + str1 + str2
#     return concat_string

# print(short_long('abc', '123123'))

def short_long(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    else:
        return str2 + str1 + str2

print(short_long('abc', '123123'))
print(short_long('abc', 'defgh') == "abcdefghabc")
print(short_long('abcde', 'fgh') == "fghabcdefgh")
print(short_long('', 'xyz') == "xyz")