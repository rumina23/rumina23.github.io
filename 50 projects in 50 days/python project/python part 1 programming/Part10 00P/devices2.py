#create a class called MobilePhone

class MobilePhone:

    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice): #constructor

        #all variables are local only to the class constructor

        #variables: make, description, model, price

        self.make = phoneMake # input("Enter phone make: ")

        self.description = phoneDesc #input("Enter phone description: ")

        self.model = phoneModel # input("Enter phone Model: ")

        self.price = phonePrice # float(input("Enter phone price "))



    # create class method

    def discount(self):

        #calDisc is a local variable

        calDisc = self.price * 0.8

        "calDisc = phonePrice * 0.8"

        print(f"The discoun is {calDisc}")



# argmake = input("Enter phone make: ")

# argdesc = input("Enter phone description: ")

# argmodel = input("Enter phone Model: ")

# argprice = float(input("Enter phone price "))

# myPhone = MobilePhone(argmake, argdesc, argmodel, argprice)



myPhone1 = MobilePhone("Samsung", "Slim Build", "S10", 1234.67)



# how do we access the class method?

myPhone1.discount()



print(f"My phone is {myPhone1.make} and {myPhone1.description}, model {myPhone1.model} and cost {myPhone1.price}")

  # create an inner class

    class MobileStorage:

        def __init__(self, storageSize):

            self.memoryCard = storageSize

            # how do we access an inner class ?

"Method 1"

m1 = MobilePhone("Samsung", "Slim Build", "S10", 1234.67).MobileStorage("100GB")

print(f"The phone storage is: {m1.memoryCard}")

# how do we access an inner class ?

"Method 1"

m1 = MobilePhone("Samsung", "Slim Build", "S10", 1234.67).MobileStorage("100GB")

print(f"The phone storage1 is: {m1.memoryCard}")



"method 2"

myInnerStorage = MobilePhone.MobileStorage("200GB")

print(f"The phone storage2 is: {myInnerStorage.memoryCard}")



"method 3"

myInnerStorage1 = myPhone1.MobileStorage("300GB")

print(f"The phone storage3 is: {myInnerStorage1.memoryCard}")


#create a class called MobilePhone

class MobilePhone:

    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice): #constructor

        #all variables are local only to the class constructor

        #variables: make, description, model, price

        self.make = phoneMake # input("Enter phone make: ")

        self.description = phoneDesc #input("Enter phone description: ")

        self.model = phoneModel # input("Enter phone Model: ")

        self.price = phonePrice # float(input("Enter phone price "))



    # create class method

    def discount(self):

        #calDisc is a local variable

        calDisc = self.price * 0.8

        "calDisc = phonePrice * 0.8"

        print(f"The discounted price is £{calDisc}")



    # create an inner class

    class MobileStorage:

        def __init__(self, storageSize):

            self.memoryCard = storageSize

# create a child class

# method 1

class MobileCPU(MobilePhone): # pass in MobilePhone calss as a parameter

    # this is the MobileCPU class constructor

    def __init__(self, phoneCPU, phoneMake, phoneDesc, phoneModel, phonePrice):

        # import the parent class copnstructor

        MobilePhone.__init__(self,phoneMake, phoneDesc, phoneModel, phonePrice)

        self.processor = phoneCPU

         method 2

class ScreenSize(MobilePhone):

    def __init__(self, phoneSSize, phoneMake, phoneDesc, phoneModel, phonePrice):

        super().__init__(phoneMake, phoneDesc, phoneModel, phonePrice)

        self.screenSize = phoneSSize

        