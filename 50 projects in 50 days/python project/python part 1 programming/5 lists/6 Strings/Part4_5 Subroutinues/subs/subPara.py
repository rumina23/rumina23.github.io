def userDetails(paraFname, paraLname,paraInterests):
  print(
f"Your first name is: {paraFname}\nYour last name is: {paraLname}\nYour interests include{paraInterests}"

    )



userDetails("Anna", "Smith", "Badminton")



argfName     = input("What is your first name? ")

argLname      = input("What is your last name?")

argInterests  = input("Do you have any interests?")

userDetails(

    input("What is your first name? "),

    input("What is your last name? "),

    input("Do you have any interests? "),

)



userDetails(argfName,argLname,argInterests)
