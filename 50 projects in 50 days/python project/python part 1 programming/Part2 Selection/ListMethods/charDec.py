


# chr(): takes a decimal and returns the ascii equivalent
# ord(): takes a character and returns the decimal equivalent

# chr(): takes a decimal and returns the ascii equivalent

# ord(): takes a character and returns the decimal equivalent



aChar = input("Enter a character: ")

convertAchar = ord(aChar)

print(convertAchar)




def alphabets():

    alphabetList = []  # creates an empty list

    for letters in range(45, 123):  # letters = 95, 96,97.....122

        alphabetList.append(chr(letters))

    return alphabetList




print(alphabets())

