"""A record is a static data structure. You must determine the attributes and the data types for each entity

during declaration. These will then be fixed for each record used in the database. Python does not have

a native data structure for a record.  data structure called a dictionary to represent a record.  A

dictionary has some of the features of a record.

A dictionary has key value pairs and is mutable in nature.  We use square brackets to declare a dictionary"""

"""A record is a static data structure. You must determine the attributes and the data types for each entity

during declaration. These will then be fixed for each record used in the database. Python does not have

a native data structure for a record.  data structure called a dictionary to represent a record.  A

dictionary has some of the features of a record.

A dictionary has key value pairs and is mutable in nature.  We use square brackets to declare a dictionary"""



# create a dictionary

dict1 = {1: "Jenny"}  # is a record in a dictionary

# adictionary with three records

dict2 = {1: "Jane Smith", 2: "Paul Smith", 3: "Adam Gordon"}

print(dict1, dict2)



print(dict2[3])

print(dict2[2])

courses = {1: "SDLC", 2: "HTML", 3: "CSS", 4: "JS", 5: "MySQL", 6: "NoSQL", 7: "Python"}

print(courses.items())



# print  using the key method

dkeys = courses.keys()

print(f"List of keys {dkeys}")



for aKey in dkeys:

    # aKey == 1,2,3,4...

    print(aKey)