"""
The input() function : allow the program to take in user input.
String is the default data type for the input function.
"""
# The values are all hardcoded to their respective variables
# num = 10
# name = "Anna"
# The input() takes user input and pass it to the varible num1
# # The input() takes user input and pass it to the varible num2
# To overwrite the default string data type for the input function
# cast the input() to the data type you want to use

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
sum = num1 + num2
print(f"The total is {sum}")



num3 = float(input("Enter your first number: "))
num4 = float(input("Enter your second number: "))
sum1 = num3 * num4
print(f"The total is {sum}")

firstName =input("write your name: ")
lastName =input("write your last name:")
interest =input("write your last interest")

print(f"Hello{firstName}\n{lastName}\n{interest}")


