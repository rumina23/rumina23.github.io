"""

Subroutine is a sewuence of instructions/code block to perform a specific task

with an identifiable name

A subroutine does not have a return statement

def is a keyword use to define a suboutine, followed by the name of the subroutine

A subroutine is not executed unless it is invoke/call

"""


# syntax  keyword name

def username():  # define a subroutine called username

    first_name = input("What is your first name?")

    print(f"Your first name is{first_name}")

    username()  # call/invoke the subroutine
    print("Welcome to the program")



username()  # call/invoke the subroutine



print("It is a beautiful day")



username()  # call/invoke the subroutine

# syntax  keyword name

def username():  # define a subroutine called username

first_name = input("What is your first name?")
last_name = input("What is your last name?")
interests = input("Do you have any interests?")

print(
  f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests includes{interests}"
  
)



