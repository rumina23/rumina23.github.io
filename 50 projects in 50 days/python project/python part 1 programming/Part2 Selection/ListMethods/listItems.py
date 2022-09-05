"index =  0,1,2,3,4,5,6............"

aList = [1,2,3,4,5,6,]

bList = [7,8,9,10,11,12]

print(aList)

print(bList)



print(aList[2])

print(bList[2])

# Add values/items form lists A and B into a new list

listAB = [

    # aList = [1, 2, 3, 4, 5, 6]

    # bList = [7, 8, 9, 10, 11, 12]

    # listAB = [8 , 10, 12, 14, 16, 18"]

    aList[i] + bList[i]

    for i in range(len(aList))

]

print(listAB)

# combine/join list

joinedList =     aList + bList

print(joinedList)

twoItems =  aList[2] + bList[4]

print(f"Added only two items  {twoItems}")

sliceItems = aList[0:2] + bList[1:4]

print(f"Slice list itemss  {sliceItems}")

cList = [1, 2, 3, 10, 11, 12, 4, 5, 6]

dList = [7, 8, 9, 4, 5, 6, 10, 11, 12]



commonNums = [nums for nums in cList if nums in dList]

print(f"The common list items for cList and dList: {commonNums}")

commonNums.sort(reverse=True)

print(f"The common list items for cList and dList: {commonNums}")

namesA = ["Anna", "Lucy", "Paul", "Jame", "Tom", "Joe"]

namesB = ["Ann3", "LuKe", "Paul", "Jame", "Tim", "Joe"]



commonNames = [names for names in namesA if names in namesB]

print(f"The common names in namesA and namesB are: {commonNames}")

allNums = [

    #   0,      1,      2,       3,    4,     5,    6

    ["Anna", "Lucy", "Paul", "Jame", "Tom", "Joe", "Liam"],  # 0

    [1, 2, 3, 10, 11, 12, 13],  # 1

    ["SDLC", "HTML", "CSS", "JS", "MySQL", "NoSQL", "Python"],  # 2

]



# print(allNums[0][0], allNums[1][0], allNums[0][0][0])

print(allNums[0][0], allNums[1][0], allNums[2][0])

print(allNums[0][1], allNums[1][1], allNums[2][1])



checkItems = int(input("Enter a number: "))

for aList in allNums:

    # print(f"Printed all items in the 3D list\n{items}")

    print(aList)

    # print(aList[:3])

    for items in aList:

        # checkItems = int(input("Enter a number: "))

        if items == checkItems:  # 11:  # checkItems:

            print(f"Found {items}")

print("Enumerate......................")

# The enumerate object yields pairs containing a count

# (from start, which defaults to zero) and a value yielded by the iterable argument.

for aList, items in enumerate(allNums):

    print(f"This is list {aList} and items {items}")

    print("Enumerate......................")

# The enumerate object yields pairs containing a count

# (from start, which defaults to zero) and a value yielded by the iterable argument.

for aList, items in enumerate(allNums):

    print(f"This is list {aList} and items {items}")

    for iPosition, anItem in enumerate(items):

        print(f"This is list {aList}, index position{iPosition}and item/element value {anItem}")

        print("Enumerate......................")

# The enumerate object yields pairs containing a count

# (from start, which defaults to zero) and a value yielded by the iterable argument.

for aList, items in enumerate(allNums):

    print(f"This is list {aList} and items {items}")

    for iPosition, anItem in enumerate(items):

        print(

            f"This is list {aList}, index position {iPosition} and item/element value {anItem}"

        )



    if iPosition == 2:  # checkItems

        print(f"Found {iPosition}")

    else:

        print(f"Not found {iPosition}")


