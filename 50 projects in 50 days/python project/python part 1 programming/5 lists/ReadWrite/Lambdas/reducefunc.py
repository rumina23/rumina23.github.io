"""The map function expects two arguments: a function and a list.
It takes that function and applies it to every element in the list,
returning the list of modified elements as a map object.
The list function is used to convert the resulting map object back into a list again."""


numList =   [1, 2, 3, 4,5,6,7,8,9,10, 11, 12]



multiplyN = 5 # int(input("Enter name: "))



result = list(map(lambda num: num * multiplyN, numList))

print(result)

rom functools import reduce



"""Reduce is another cool Python function. It applies a rolling calculation to all items in a list.

You could use this to tally up a sum total, or multiply all numbers together:"""



numList =   [1, 2, 3, 4,5,6,7,8,9,10, 11, 12]

"        num1 +num2 = ans, num1(ans) + num2 = ans......       "

        #    1+2=3, 3+2=5, 5+3= 8



print(f"original numbers: {numList}")



rolledNums = reduce(lambda num1, num2: num1 + num2,  numList)

print(f"Rolling numbers: {rolledNums}")