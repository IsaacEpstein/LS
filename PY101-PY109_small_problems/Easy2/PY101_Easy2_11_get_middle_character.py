"""
PY101-PY109_small_problems

Easy2
11 Get Middle Character
Write a function that takes a non-empty string argument and returns the 
middle character(s) of the string. If the string has an odd length, you 
should return exactly one character. If the string has an even length, 
you should return exactly two characters.

PEDAC
P:
input: a non empty string
output: the middle character(s)
requirements: create a function and return one if odd and two if even

E:
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True

D:
input: string
output: string

A:
initialize a function which takes a string as an argument
if the string is of odd length, return the middle character
if the string is of even length, return the two middle characters

C:
"""
def center_of(string):
    if len(string) % 2 != 0:
        return string[len(string) // 2]
    else:
        return string[(len(string) // 2 - 1):((len(string) // 2) + 1)]
    
print(center_of('I Love Python!!!')) # == "Py")   
print(center_of('Launch School')) #== " ")        
print(center_of('Launchschool')) #== "hs")        
print(center_of('Launch')) # == "un")             
print(center_of('Launch School is #1')) #== "h")  
print(center_of('x')) #== "x")                    