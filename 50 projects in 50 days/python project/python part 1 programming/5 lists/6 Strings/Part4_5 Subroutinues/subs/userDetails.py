# create a dictionary

"name  = {key:value, key:value,  key:value, key:value, key:value, key:value}"

dict2 = {1: "Jane Smith", 2: "Paul Smith", 3: "Adam Gordon"}



userDetails = {"fName": "", "course": "", "module": ""}



# use the input function to ask for user data

userDetails["fName"] = input("Enter your full name: ")

userDetails["course"] = input("Enter your course name: ")

userDetails["module"] = input("Enter module name: ")



print(userDetails)

# print  using the key method

userValues = userDetails.values()

print(f"List of values {userValues}")



for aValue in userValues:

    # aKey == 1,2,3,4...

    print(aValue)

    # create a dictionary with  no keys and no values

userDetails1 = {}  # creae an empty dictionary

dictKey1 = input("Enter a key: ")  # ask for a key = age

userDetails1[dictKey1] = input(f"Enter a value for :{[dictKey1]} ")

print(userDetails1)

userDetails1 = {}  # creae an empty dictionary

dictKey2 = input("Enter a key: ")  # ask for a key = age

userDetails1[dictKey2] = input(f"Enter a value for :{[dictKey2]} ")

print(userDetails1)

 create a dictionary

"name  = {key:value, key:value,  key:value, key:value, key:value, key:value}"

dict2 = {1: "Jane Smith", 2: "Paul Smith", 3: "Adam Gordon"}



# create a dictionary with keys but no values

userDetails = {"fName": "", "course": "", "module": ""}



# use the input function to ask for user data

userDetails["fName"] = input("Enter your full name: ")

userDetails["course"] = input("Enter your course name: ")

userDetails["module"] = input("Enter module name: ")



print(userDetails)



# print  using the key method

userValues = userDetails.values()

print(f"List of values {userValues}")



for aValue in userValues:

    # aKey == 1,2,3,4...

    print(aValue)




# create a dictionary with  no keys and no values

userDetails1 = {}  # creae an empty dictionary

dictKey1 = input("Enter a key: ")  # ask for a key = age

userDetails1[dictKey1] = input(f"Enter a value for :{[dictKey1]} ")

print(userDetails1)



userDetails1 = {}  # creae an empty dictionary

dictKey2 = input("Enter a key: ")  # ask for a key = age

userDetails1[dictKey2] = input(f"Enter a value for :{[dictKey2]} ")

print(userDetails1)




if dictKey1 == dictKey2:

    print("Same Key")