class Developer:

    def __init__(self):

        self.name = ""

        self.salary = ""



    # create a getter method

    def getName(self):

        return self.name #return the value passed in to the variable

   

    def getPay(self):

        return self.salary



"Method 1"

# create an object from class developer

dev1 = Developer()



# set the values for the respective variables(name and salary) in the class

dev1.name = "Anna"

dev1.salary= 1234.56

print(f"{dev1.name} is paid {dev1.salary} as a developer")

# create an object from class developer

dev2 = Developer()



# set the values for the respective variables(name and salary) in the class

dev2.name = "Lucy"

dev2.salary= 2234.56

print(f"{dev2.getName()} is paid {dev2.getPay()} as a developer")

