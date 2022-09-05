s1 = "I am a python programmer"
s2 = "I am a python programmer with single quote"
s3 = """I am a python programmer, pytjon is great, widely use for all things software related.
Data science, full stack and front end"""

s4 = " How are you "

# exerise: print characters in position 10, 16 and 20 from s2
# exerise: print two characters from any of the strings above by index
# exerise: print the length of any string

print(len(s1))
print(len(s2))
print(len(s3))
print(len(s4))

# exerise: print characters in position 10, 16 and 20 from s2

print(s2[10], s2[16], s2[20])

print(s1[10], s2[26], s3[30])



# exerise: print two characters from any of the strings above by index
print(s2[5:7])
# exerise: print the length of any string
print(f"The length of the list is: {len(s1)}")

# Slicing string using start and end index
print(s2[2:20]) # start index and end index
print(s2[2:])  # start index and  no end index
# print(s2)
print(s2[:])  # No start index and  no end index
print(s1[5:-1])

print(s1[5:-1])
print(s1[5:-2])
print(s1[5:-3])
print(s1[5:-4])

# steps

s5 = "Dangerous"
print(s5)

# slice string using start, end index and specify the steps

print(s5[1:8:2])  # start, end and step
print(s5[1::2]) # start, no end and step
print(s5[::2]) # no start, no end and step

# stripping white spaces

" How are you "

print(s4)

print(s4.lstrip()) #strip white spaces from the left/start of the string

print(s4.rstrip()) #strip white spaces from the right/end of the string

print(s4.strip()) #strip white spaces from the right and left/ start and end of the string

print(f"The number of a: {s3.count('a')}") # count the number of times a characters appears in a string

# replace a substring

print(s4.replace("How", "Where"))

print(s4)

# Use upper, lower and title methods

print(f"Upper case {s4.upper()}")

print(f"Lower case {s4.lower()}")

print(f"Title case {s4.title()}")

# use the split method and join method

jointxt = "".join(s4.split())

print(jointxt)

name = "Rumina"

print(name)

charactersInName = name.split()

print(charactersInName)

name = "Welcome to python"

print(name)

charactersInName = name.split()

print(charactersInName)




