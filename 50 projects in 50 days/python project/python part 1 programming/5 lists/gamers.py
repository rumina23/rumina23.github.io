playersList = []  # create an empty list

addPlayer = True  # flag varible of boolean Type set to True



while (

    addPlayer

):  # While True execute the code bloew until the conditin is no longer True

    # ask for user input respectively

    pName = input("Enter player name:")

    pPass = input("Enter player password:")

    pScore = int(input("Enter player current score:"))

    pHscore = int(input("Enter player high score:"))



    # create dictionary to hold player profiles

    playerProfile = {

        "playerTag": pName,

        "playerPass": pPass,

        "curScore": pScore,

        "highScore": pHscore,

    }

# add a player profile to player list

playersList.append(playerProfile)

    anotherPlayer = input("Do you want to add another player? Y/N ").upper()

    if anotherPlayer == "N":  #check/compare user response with the value "N"

        addPlayer = False # reset the value asssign to addPlayer to "False"



print(f"List of players:\n {playersList} ")

# "  0                    1                       2               3              ...................   "

# {"playerTag": "AA", "playerPass": "aPass", "curScore": 123, "highScore": 345},  #0

# {"playerTag": "BB", "playerPass": "bPass", "curScore": 56,   "highScore": 789},  #1

# {"playerTag": "CC", "playerPass": "cPass", "curScore": 678, "highScore": 9087},  #2

# {"playerTag": "DD", "playerPass": "dPass", "curScore": 3456, "highScore": 8797979,} #3



aRecord = int(input("Enter the number(index position) of the record to be displayed"))

# access a specifi player record base on the index value that matches the index position

aPlayer = playersList[aRecord]  # indx = 1

print(f"The player details are: {aPlayer} ")

# {"playerTag": "BB", "playerPass": "bPass", "curScore": 56,   "highScore": 789},  #1

aPlayerAttribute = input(f"What attribute from {aPlayer} you want to print")

# {"playerTag": "BB", "playerPass": "bPass", "curScore": 56,   "highScore": 789},  #1

print(f"The player {aPlayerAttribute} of {aPlayer[aPlayerAttribute]}:")