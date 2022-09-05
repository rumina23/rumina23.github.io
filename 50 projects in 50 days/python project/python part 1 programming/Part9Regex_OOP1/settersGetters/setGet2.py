class Developer:

    def __init__(self, devName): #devName, devSalary

        self.name =  devName

        self.salary =  ""   #devSalary

        self.job =""



    # create a getter methods

    def getName(self):

        return self.name #return the value passed in to the variable

   

    def getPay(self):

        return self.salary



      #create setter methods

    def getJob(self ):

        return self.job

       

    #create setter methods

    def setJob(self, devJob ):

        self.job = devJob



    def setPay(self, devSalary ):

     self.salary = devSalary



"Method 1"

# create an object from class developer

dev1 = Developer("James")



# set the values for the respective variables(name and salary) in the class



dev1.setJob("Python")

dev1.setPay(4056.7)

print(f"{dev1.name} is paid {dev1.salary} as a {dev1.job} developer")