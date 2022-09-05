#create a class called MobilePhone
class MobilePhone:
    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice): #constructor
        #all variables are local only to the class constructor
        #variables: make, description, model, price
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice
# How to access the properties/varibles and values inside the MobilePhone class
argmake = input("Enter phone make: ")
argdesc = input("Enter phone description: ")
argmodel = input("Enter phone make: ")
argprice = float(input("Enter phone price "))
myPhone1 = MobilePhone(argmake, argdesc, argmodel, argprice)
print(f"My phone is {myPhone1.make} and {myPhone1.description}, model {myPhone1.model} and cost {myPhone1.price}")

myPhone2 = MobilePhone("Samsung", "Gorilla Glass", "S10 +", 234.56)
print(f"My phone is {myPhone2.make} and {myPhone2.description}, model {myPhone2.model} and cost {myPhone2.price}")