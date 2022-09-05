"""patterns that help a user match character combinations
in text files and strings. You can use regular expressions to filter or find a
specific pattern in the output of a  command or a document."""

import re

"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string
contains alphanumeric characters including underscores.
For example,\w will match a, b, c, d, 1, 2, 3, etc."""

sentence = "Take up one python project Idea. One project idea at a time and build something"

sentence = "Take up one python project Idea. One project idea at a time and build something"

#Search function: Scan through string looking for a match to the pattern, returning

# a Match object, or None if no match was found.

searchString = re.search(r"o\w\w",sentence)



# The group method is a method on the result that came back which gives the exact substring

# that matches the pattern specified in the search

print(f"Search result: {searchString.group()}")

searchString = re.search(r"i\w\w\w",sentence)
print(f"Search result: {searchString1.group()}")

