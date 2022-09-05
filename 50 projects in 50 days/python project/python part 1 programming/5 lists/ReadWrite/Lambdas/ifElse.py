compareNums = lambda num1: "Even Number" if num1 % 2 == 0 else "Odd Number"

print(compareNums(21))

print(compareNums(22))

userCheck = lambda userName: print(f"Your username is : {userName}") if len(userName) >5 else print(f"invalid: {userName}")

name = input("Enter username: ")

userCheck(name)