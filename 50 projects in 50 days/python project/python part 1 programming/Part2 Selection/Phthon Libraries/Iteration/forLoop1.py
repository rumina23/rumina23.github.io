"""

use a for loop when the number of iteration is known(how many times you want/going to do something for)

A for loop also controls the flow of execution in a program

"""
#Iteration means to repeat in programming



"syntax "

# for variablename in range method(numberofIteration)

for findNumber in range(10): # we specify the number of iterations

    print(findNumber)
    # Delay execution for a given number of seconds.

# The argument may be a floating point number for subsecond precision.

sleep(2)

print("using start and stop")

# for variablename in range method(startNum, endNum)

for findNumber in range(5, 10):  # we specify the start and stop values

    print(findNumber)

    sleep(3)

print("using start, stop and step")

# for variablename in range method(startNum, endNum and step)

for findNumber in range(5, 56, 10):  # we specify the start, stop and step values
print(findNumber)

  print("count down")
for findNumber in range(10,5,-1):  # we specify the start and stop values
    print(findNumber)


    
