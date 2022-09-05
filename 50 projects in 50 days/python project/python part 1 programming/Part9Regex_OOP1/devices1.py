"""To understand the meaning of classes we

have to understand the built-in __init__() function.

All classes have a function called __init__(), which is

 always executed when the class is being initiated.

 Use the __init__() function to assign values to object

 properties, or other operations that are necessary to do

 when the object is being created"""

 # What is a contructor in python?

"It is a method that is called when an object is created "

"This method is defined inside the class and can be used to initialise variables"



# What is a class?

"A blueprint/template"



# What is an object?

"An instance of a class"

#create a class called MobilePhone

class MobilePhone:

    def __init__(self): #constructor

        #all variables are local only to the class constructor

        #variables: make, description, model, price

        self.make = "Samsung"

        self.description = "Slim Build"

        self.model = "Galaxy S22"

        self.price = 899.99



# How to access the properties/varibles and values inside the MobilePhone class



myPhone1 = MobilePhone() # create an object from the MobilePhone Class

"Use the object (myPhone1) to access properties/varibles and values inside the MobilePhone class"

print(myPhone1.description)

# Execise Access the other values held in the other three variables
"Solutions"
print(myPhone1.description)
print(myPhone1.model)
print(myPhone1.price)

myPhone2 = MobilePhone()

myPhone2.make = "Apple"

myPhone2.description = "IPS Display"

myPhone2.model = "Iphone 11"

myPhone2.price = 1099.89



print(myPhone2.make)
print(myPhone2.description)
print(myPhone2.model)
print(myPhone2.price)

myPhone3 = MobilePhone()
myPhone3.make = input("Enter phone make: ")
myPhone3.description = input("Enter phone description: ")
myPhone3.model = input("Enter phone make: ")
myPhone3.price = float(input("Enter phone make: "))
print(myPhone3.make)
print(myPhone3.description)
print(myPhone3.model)
print(myPhone3.price)
print(f"My phone is {myPhone3.make} and {myPhone3.description}, model {myPhone3.model} and cost {myPhone3.price}")




 