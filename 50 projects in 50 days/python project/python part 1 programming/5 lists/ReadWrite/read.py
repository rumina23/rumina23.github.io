#variable = openMethod(filepath/filename, "mode")

# Part7 Dict_DataFiles\3 ReadWrite\file1.txt

file1Path = open("Part7 Dict_DataFiles/3 ReadWrite/file1.txt", "r") #open file path

readFile1 = file1Path.read()  # read the file content

print(readFile1) # print file contents

file1Path.close()

"Method 2: Contet+xt Manager"

with open("Part7 Dict_DataFiles/3 ReadWrite/file1.txt", "r") as file1Path:

    readFile1 = file1Path.read()  # read the file content

    print(readFile1) # print file contents






