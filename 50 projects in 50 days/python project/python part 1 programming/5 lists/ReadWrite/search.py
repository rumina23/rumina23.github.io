# To search a file

time.sleep(3)

searchFile = input("Enter search keyword: ")

with open("Part7 Dict_DataFiles/3 ReadWrite/userDetails.txt", "r") as userSearch:

    readFile = userSearch.read()



if searchFile in readFile:

    print(f"Found {searchFile}")

else:

    print(f"Not Found {searchFile}")
