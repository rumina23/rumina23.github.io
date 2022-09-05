from sub1 import username
from time import sleep



print("Welcome.................")
sleep(2)
#username()  # call/invoke the suboutine username

def sub():

    num1 = int(input("Enter your first number: "))

    num2 = int(input("Enter your second number: "))

    sum = num1 - num2

    print(f"The total is {sum}")




def multiply():

    num1 = int(input("Enter your first number: "))

    num2 = int(input("Enter your second number: "))

    sum = num1 * num2

    print(f"The total is {sum}")