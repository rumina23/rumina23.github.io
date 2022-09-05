def username(first_name, last_name, interests):  # define a subroutine called username

    statement = (

        f"Your name is {first_name} {last_name}, and your interests are {interests}"

    )

    return statement



first_name = input("What is your first name? ")

last_name = input("What is your last name? ")

interests = input("Do you have any interests? ")

print(f"{username(first_name, last_name, interests)}")



userdetails = username(

    input("What is your first name? "),

    input("What is your last name? "),

    input("Do you have any interests? "),

)



print(userdetails)