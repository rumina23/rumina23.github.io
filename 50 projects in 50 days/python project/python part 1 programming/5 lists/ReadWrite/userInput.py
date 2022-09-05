import time



userName = input("Enter your username: ")

fullName = input("Enter your Fullname: ")

userAge = int(input("Enter your username: "))



with open("Part7 Dict_DataFiles/3 ReadWrite/userDetails.txt", "a") as file1Path:

# method 1
# writeToFile = file1Path.write(f"{userName}\n{fullName}\n{userAge} ")  # write to a file

  writeToFile = file1Path.write("\n" +userName + " " + fullName + " " + str(userAge))  # write to a file

   # Method 3

    userData = "\n" + userName + " " + fullName + " " + str(userAge)

    file1Path.write(userData)

       # Method 4: Using a list



    userDataList = [] # create an empty list

    # add data to list

    userDataList.append(userName)

    userDataList.append(fullName)

    userDataList.append(userAge )



    strData = str(userDataList) #convert list to string

    file1Path.write(f"\n{strData}")

    file1Path.write(f"\n'This is the Data List\n'{userDataList}")

    # write to file

with open("Part7 Dict_DataFiles/3 ReadWrite/userDetails.txt", "a") as file1Path:

    strData = str(playersList) #convert list to string

    file1Path.write(f"\n{strData}")