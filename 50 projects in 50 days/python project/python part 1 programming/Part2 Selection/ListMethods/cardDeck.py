# ♥ ♦ ♣ ♠

from random import shuffle



suits = ["♥", "♦", "♣", "♠"]

deck = []



for aSuit in suits:

    # print(aSuit)

    for aCard in range(1, 14):

        if aCard == 11:

            # change/ replace the value 11 to "J" and add it to to the empty list deck

            deck.append("J" + aSuit)

        elif aCard == 12:

            deck.append("Q" + aSuit)

        elif aCard == 13:

            deck.append("" + aSuit)

        elif aCard == 1:

            deck.append("A" + aSuit)

        else:

            deck.append(str(aCard) + aSuit)

print(deck)

shuffle(deck)

print(f"Shuffled deck\n {deck}")