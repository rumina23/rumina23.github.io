cardvalue = "Kings"

suitOfcards = "Hearts"



chkCardValue =  input("Enter card value: ").title()

chkCardSuit =  input("Enter card suit: ").title()



# use the and operator  

if cardvalue == chkCardValue and suitOfcards == chkCardSuit:

    print("Winner!")

else:

    print("Try Again")

    ageCheck = 18

userAge = 25

if ageCheck >= userAge:

 print(f"Age verification complete!")
