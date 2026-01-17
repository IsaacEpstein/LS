"""
PY101-PY109_small_problems

Easy2
6 The End Is Near But Not Here
Write a function that returns the next to last word in the string argument.
Words are any sequence of non-blank characters.
You may assume that the input string will always contain at least two words.

PEDAC
P:
input: string
output: 2nd to last word in a string
requirement: write a function which takes a string argument

E:
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

D:
input: string
output: string

A:
define a function which takes a string argument
split the string into words and then print the second to last

C:
"""
# def penultimate(sentence):
#     return sentence.split(' ')[-2]

# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")


# Our solution ignored two edge cases since we explicitly stated that 
# you didn't have to handle them: strings that contain no words or just 
# one word.

# Suppose we need a function that retrieves the middle word of a 
# phrase/sentence. What edge cases need to be considered? How would you 
# handle those edge cases without ignoring them? Write a function that 
# returns the middle word of a phrase or sentence. It should handle all 
# of the edge cases you thought of.

# def middle(sentence):
#     if not sentence.split():
#         print('Sentence contains no words')
#     elif len(sentence.split()) == 1:
#         print('This sentence only has one word.')
#     else:
#         words = sentence.split()
#         if len(words) % 2 == 0:
#             print('There is no middle word.')
#         else:
#             return sentence.split()[(len(words) // 2)]
        
# print(middle(""))        
# print(middle("  "))
# print(middle("My name Isaac Epstein"))
# print(middle("My name is Isaac Epstein"))

def middle(sentence):
    words = sentence.split()

    if not words:
        return "No words"
    elif len(words) == 1:
        return "Only one word"
    elif len(words) % 2 == 0:
        return "There is no middle word"
    else:
        return words[len(words) // 2]
        
print(middle(""))        
print(middle("  "))
print(middle("My name Isaac Epstein"))
print(middle("My name is Isaac Epstein"))