import re

# \d  = 0-9 , \D = non digit characters, \s = white space , \S = non white space

sentence = "Take up ox2ne o python o6n project one3 Idea one o8wn ore. oo oof One pro7ject  idea at a t7ime and build something"

# Split the source string by the occurrences of the pattern,

# returning a list containing the resulting substrings

#

print(sentence)

searchString = re.split(r"\d", sentence)

print(f"Search result numeric : {searchString}")



searchString1 = re.split(r"\D", sentence)

print(f"Search result non numeric : {searchString1}")



searchString2 = re.split(r"\s", sentence)

print(f"Search result white space: {searchString2}")

searchString3 = re.split(r"\S", sentence)

print(f"Search result non white space : {searchString3}")