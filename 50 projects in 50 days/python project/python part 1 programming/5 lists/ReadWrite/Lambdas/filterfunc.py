"""With the filter function, the process is much the same.
Filter takes a function and applies it to every element in a list
and created a new list with only the elements that caused the function to return True."""

c11People = ["Anna", "Lucy", "Paul", "Jame", "Tom", "Joe", "Liam"]

nums =   [1, 2, 3, 4,5,6,7,8,9,10, 11, 12, 13]



print(f"original numbers: {nums}")



filteredNums = list(filter(lambda evenNums: evenNums % 3 == 0, nums))



print(f"filtered numbers: {filteredNums}")
search = input("Enter name: ")

c11People = ["Anna", "Lucy", "Paul", "Jame", "Tom", "Joe", "Liam"]

foundP = list(filter(lambda aPerson: aPerson == search, c11People))

print(f"List of peaople: {c11People}")

print(f"Found the person : {foundP}")