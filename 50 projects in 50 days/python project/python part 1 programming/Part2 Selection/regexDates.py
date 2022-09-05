import re

# \d  = 0-9 , \D = non digit characters, \s = white space , \S = non white space

sentence = "Take up ox2ne o python o6n project one3 Idea one o8wn ore. oo oof One pro7ject  idea at a t7ime and build something"



print(sentence)

#Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.

searchString = re.match(r"o\w\w", sentence)

print(f"Search result  : {searchString}")



searchString1 = re.match(r"T\w\w", sentence)

print(f"Search result  : {searchString1}")




searchString2 = re.match(r"T\w\w", sentence)

#Only invoke the group method if there is a match at the start of the string

print(f"Search result  : {searchString2.group()}")

searchString2 = re.findall(r"\d{1,2}-\d{1,2}-\d{1,4}", sentence)

print(f"Search result  : {searchString2}")



searchString3 = re.findall(r"\d{1,2}-\d{1,2}-\d{4}", sentence)

print(f"Search result  : {searchString3}")