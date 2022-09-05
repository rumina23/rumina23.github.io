"""

A function is a sequence of instructions/code block to perform a specific task

with an identifiable name

A function returns a value, has a return statement

def is a keyword use to define a suboutine, followed by the name of the subroutine

A subroutine is not executed unless it is invoke/call

"""



def multiply():

    num1 = int(input("Enter your first number: "))

    num2 = int(input("Enter your second number: "))

    sum = num1 * num2



    return sum # value held in total will be returned when the multiply function is invoked/called



print("Method 1")

print(f"The total is {multiply()}")



print("Method 2")

myMultiply = multiply()

print(f"The total is {myMultiply}")

def addition():

    total = 10 + 20

    return total


print(f"The total is {addition()}")
def multiply(paraNum1, paraNum2):

    sum = paraNum1 * paraNum2

    return sum  # value held in total will be returned when the multiply function is invoked/called




argNum1 = int(input("Enter your first number: "))

argNum2 = int(input("Enter your second number: "))



print("method 1")

print(f"Your answer is{multiply(argNum1,argNum2)}")
print("method 2")

myMul = multiply(argNum1,argNum2)

print(f"Your answer is{myMul}")




print("method 3")

myMul = multiply(21,34)

print(f"Your answer is{myMul}")


# exercise :modify the code below and put it into a function with parameters

def username():  # define a subroutine called username

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
interests = input("Do you have any interests? ")
print(
   f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}"
)
