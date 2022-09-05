"""use a while loop when the number of iteration is unknown(dont know how many times you want/going

to do something for)

A while loop also controls the flow of execution in a program"""

# While loop keeps looping/iterating until a condition is met



userGuess = input("Enter guess word: ")

guessWord = "Cohort11"



while userGuess != guessWord:

    #ask user to keep guessing ...again again ...again .again again ..]

    # .again until thee guessed(Cohort11): condition met

    userGuess = input("Guess again!: ")

print(f"You guessed {userGuess} correctly")