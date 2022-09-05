"""A lambda is simply a way to define a function in Python. They are sometimes known as "lambda
operators" or "lambda functions".  A lambda function is a small anonymous function, they are funct
that don't need to be named. They are used to create small, one-off functions in cases where a "re
function would be too big and bulky.   A lambda function can take any number of arguments, but can
only have one expression."""

# Standard python function

def myFunc():

    add = 2 + 5

    return add

add = myFunc()

print(add)



"lambda operators or lambda functions "

# variable = lambda arguments : expression



addNum = lambda num1: num1 + 21



print(addNum(45))

addNum = lambda num1, num2: num1 + 21 + num2 + 10

print(addNum(45, 12))

addNum3 = lambda num1, num2: num1 + 21 + num2 + 10

argNum1 = int(input("Enter the first number: "))

argNum2 = int(input("Enter the first number: "))

print(addNum3(argNum1, argNum1))
addNum3 = lambda num1, num2: num1 + num2 + 21 + 10

argNum1 = int(input("Enter the first number: "))

argNum2 = int(input("Enter the second number: "))

print(addNum3(argNum1, argNum2))