"""
Data types are nothing but variables use to hold/ reserve a space in memory
Variables i python do not neeed an explicit declaration to reserve memory space
The declaration of the the data type happens automatically
when the variable is initalised with a value/ assign a value

"""
# string  datatype
firstname = "Jane"
fullname = "Anna Doe"
name = ""  # initialised a variable with and empty string
sentence = """

This is a sentence
This is a sentence
This is a sentence
This is a sentence
"""

print(type(firstname))
print(type(fullname))
print(type(name))
print(type(sentence))

# mumeric data types
num1 = 12  # integer
num2 = 12.5  # float
print(type(num1))
print(type(num2))

"""

List is an ordered sequence of items. It is also flexible data type in python
The values in a list does not have to be of the same data
type and the items can be modify

"""
#              0      1      2       3   4  5 6   7     8
c11Devs = ["Anna", "Paul", "Joe", "Jane", 1, 2, 3, -12, num1]
print(type(c11Devs))
print(c11Devs[6])  # access items from the list by their index value

# Boolean data types: True/False

boolval1 = False
boolval2 = True
print(type(boolval1))
print(type(boolval2))

 #dictionary store data in key value pairs

"                  key: value"
dictionary1 = {1: "Jane Smith", "course": "Python"}
print(type(dictionary1))
print(dictionary1["course"])
print(dictionary1[1])

print(f"Prints every data held in the dictionary\n{dictionary1} ")
