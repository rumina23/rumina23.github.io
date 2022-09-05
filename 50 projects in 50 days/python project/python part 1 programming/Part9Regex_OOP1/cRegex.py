import re



"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string

contains alphanumeric characters including underscores.

For example,\w will match a, b, c, d, 1, 2, 3, etc."""



sentence = "Take up one o python on project one Idea one own ore. oo oof One project  idea at a time and build something"

#Return the string obtained by replacing the leftmost non-overlapping

# occurrences of the pattern in string by the replacement rep

searchString = re.sub(r"one", "two", sentence)

print(f"Search result : {searchString}")

# exercise modify the pattern in the searchString to use the +, * and ? operators

searchString1 = re.sub(r"o\w+", "two", sentence)

print(f"Search result : {searchString1}")

searchString2 = re.sub(r"o\w*", "two", sentence)

print(f"Search result : {searchString2}")

searchString3 = re.sub(r"o\w?", "two", sentence)

print(f"Search result : {searchString3}")



