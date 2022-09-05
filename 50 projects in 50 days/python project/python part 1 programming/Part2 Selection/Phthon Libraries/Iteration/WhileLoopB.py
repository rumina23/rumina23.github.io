# While loop keeps looping/iterating until a condition is met



userGuess = input("Enter guess word: ") # first attempt to enter guess word

guessWord = "Cohort11"

guessAttempts = 1 # flag variable guessAttempts = 1



while userGuess != guessWord and guessAttempts < 3:

    # ask user to keep guessing ...again again ...again .again again ..]

    # .again until thee guessed(Cohort11): condition met

    userGuess = input(f"Try again!: You have guessed {guessAttempts} /3 attempts ")

    guessAttempts += 1   # guessAttempts = guessAttempts + 1



if userGuess == guessWord:

    print(f"You guessed {userGuess} correctly")

else:

    print(f"You have used  {userGuess} {guessAttempts} /3 attempts")