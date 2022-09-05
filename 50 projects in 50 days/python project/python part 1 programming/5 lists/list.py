c11 = [
"Anna",  # 0
"Paul",  # 1
"Joe",  # 2
"Jane",  # 3
"Anne",  # 4
"Pauline",  # 5
"Joan",  # 6
"Janet",  # 7

]

lstScores = [10, 20, -5, 1, 56, 78, 13]

lstModules = ["HTML", "CSS"]

print(lstModules)

# insert item to a list using the index position



"index position, item"

lstModules.insert(0, "SDLC")

print(lstModules)

lstModules.insert(2, "JS")

print(lstModules)

# append an item to a list

lstModules.append("MySQL")
print(lstModules)
print("Slicing list items")
"    0        1      2      3       4   "
# ['SDLC', 'HTML', 'JS', 'CSS', 'MySQL']
print(lstModules[1:4])
print(lstModules[1:3])
print("End of slicing items")

print(f"The length of the list is: {len(lstModules)}")

del lstModules[1] # delete using index position
print(lstModules)

lstModules.remove("SDLC") # remove item from list by value
print(lstModules)

# sort list items

print(f"Unsorted: {lstScores}")

print(f"Sorted in ascending order: {lstScores}")

lstScores.sort(reverse=True)
print(f"Sorted in descending order: {lstScores}")

print(c11)

c11.clear()

print(f"This list has been cleared:{c11}")











