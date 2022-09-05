name = input("Enter name: ")
if name.islower(): #Return True if the string is a lowercase string, False otherwise.

print(f"Welcome {name}")

else:
print(f"Your {name} is not in lower case")
exit() # exit the program

userWord = input("Enter a word with minimum 5 characters: ")

#the condition , the output if the condition fails

assert len(userWord)>=5, "Minimum 5 characters required"

print("You met the requirement")

userWord2 = input("Enter the secret word: ")

# the condition , the output if the condition fails

assert userWord2 == "superwoman", "That is not the secret word"

print("You have entered the secret word")

userNum2 = int(input("Enter a number greater than 50"))

# the condition , the output if the condition fails

assert userNum1 > 50, "Number etered must be greater than  50"

print("You have entered a number greater than 50")

{names}")

# print("Welcome")




try:

    name = input("Enter your name: ")

    print(f"your name is {names}")



except NameError:

    print("Variable name doesn't exists")




print("Welcome")