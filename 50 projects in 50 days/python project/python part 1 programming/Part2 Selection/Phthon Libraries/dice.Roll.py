if dice == 12:
    dice = 0  # re-assign the value of dice to 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player1Score = dice
print(f"Player 1 Score : {player1Score}")


"Player 2"
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

print(f"Die 1: {die1}, Die 2: {die2}")

dice = die1 + die2  # value from both dice
if dice == 12:
    dice = 0  # re-assign the value of dice to 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player2Score = dice
print(f"Player 2 Score : {player2Score}")

# check/compare the values held in player1Score against player2Score
if player1Score > player2Score:
    print(f"Player 1 rolled {player1Score} and is the winner! ")
else:
    if player1Score < player2Score:
        print(f"Player 2 rolled {player2Score} and is the winner! ")
    else:
        print(
            f"Its a draw! | Player 1 rolled {player1Score} | Player 2 rolled {player2Score}"
        )