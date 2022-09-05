score =  int(input("Enter your score: "))



if score >= 75: #check if score is greater than equal to

    grade =  "A" #create a variable and assign it a value 'A'



elif score >= 60:

    grade = "B" # re-assign the value hed in grade variable to 'B'



elif score >= 50:

    grade = "C"  # re-assign the value hed in grade variable to 'C'



else:

    grade = "F"  # re-assign the value hed in grade variable to 'F'



print(f"You scored {score} and your grade is: {grade}")




