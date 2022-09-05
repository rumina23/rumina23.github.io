#create a class called MobilePhone

class MobilePhone:

    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice): #constructor

        #all variables are local only to the class constructor

        #variables: make, description, model, price

        self.make = phoneMake # input("Enter phone make: ")

        self.description = phoneDesc #input("Enter phone description: ")

        self.model = phoneModel # input("Enter phone Model: ")

        self.price = phonePrice # float(input("Enter phone price "))




# create an empty list

listOfPhones = []



while True:

    # How to access the properties/varibles and values inside the MobilePhone class

    argmake = input("Enter phone make: ")

    argdesc = input("Enter phone description: ")

    argmodel = input("Enter phone Model: ")

    argprice = float(input("Enter phone price "))



    listOfPhones.append(argmake + " " + argdesc + " " +  argmodel + " " +  str(argprice))



    anotherMobile = input("Enter another mobile?  Y/N: ").upper()

    if anotherMobile == "N": # if the condition is met

        break # exit the loop(stop adding mobile phones)



myPhone1 = MobilePhone(argmake, argdesc, argmodel, argprice)
for mobile in listOfPhones:

    print(mobile)



    with open(r"Part9 Regex_OOP1\OOP intro\file1.txt", "a") as file1:

        saveMobile = file1.write(f"\n{mobile}")




with open(r"Part9 Regex_OOP1\OOP intro\file2.txt", "a") as file2:

    phones = str(listOfPhones)

    saveMobile = file2.write(f"\n{phones}")