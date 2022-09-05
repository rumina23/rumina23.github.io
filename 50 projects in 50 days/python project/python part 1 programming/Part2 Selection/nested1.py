"""

Nested selection/nesting is when a selection block(if/else) is placed within another selection

block

"""
userAge = int(input("Enter your age: "))
ageLimit = 16
passCode = "Cohort11"

if userAge > ageLimit: # compare the value held in userAge against the value held in ageLimit
 print("You met the minimum age requirement") # execute if the condition above is met
userCode = input("Enter code: ")
if userCode == passCode: # this block is nested inside the first if 
  print(f"Your code {userCode} is valid. Access granted !")
print("closing ")


