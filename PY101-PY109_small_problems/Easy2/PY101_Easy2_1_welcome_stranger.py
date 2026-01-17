"""
PY101-PY109_small_problems

Easy2
1 Welcome Stranger
Create a function that takes 2 arguments, a list and a dictionary. 
The list will contain 2 or more elements that, when joined with spaces, 
will produce a person's name. The dictionary will contain two keys, "title" 
and "occupation", and the appropriate values. Your function should return a 
greeting that uses the person's full name, and mentions the person's title.

PEDAC
P:
input: 
1 list of strings (2 or more elements)
1 dictionary with two keys: "title" and "occupation" and values
requirements: join the strings to form a name
output: retrn a greeting with the person's name and title.

E:
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

D:
input: 
list of strings
dictionary with the two key value pairs which are strings
output: string

A:
define a function which takes two arguments
initialize a variable for the persons name and set that equal to the elements
of the list joined by spaces " ".
return a greeting which has the person's name and their occupation

C:
"""
def greetings(name, work):
    return (f'Hello, {' '.join(name)}, nice to have a {work['title']} '
            f'{work['occupation']} around.')
    # return ('Hello, ' + ' '.join(name) + ", nice to have a " + work['title']
    #             + " " + work['occupation'] + " around.")

print(greetings(["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},))