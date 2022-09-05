"""Regular expressions are patterns that help a user match character combinations

in text files and strings. You can use regular expressions to filter or find a

specific pattern in the output of a  command or a document."""



import re



"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string

contains alphanumeric characters including underscores.

For example,\w will match a, b, c, d, 1, 2, 3, etc."""

sentence = "Take up one o python on project one Idea one own ore. oo oof One project  idea at a time and build something"

#If one or more capturing groups are present in the pattern, return a list of groups;

# this will be a list of tuples if the pattern has more than one group.

searchString = re.findall(r"o\w\w",sentence)

print(f"Search result : {searchString}")



#Using the plus operator returns one or more alpha numeric character after the specified chatacter

# in the begining of the text

searchString1 = re.findall(r"o\w+",sentence)

print(f"Search result using +: {searchString1}")



#Using the asterix operator returns zero or more alpha numeric character after the specified chatacter

# in the begining of the text

searchString2 = re.findall(r"o\w*",sentence)

print(f"Search result using *: {searchString2}")

