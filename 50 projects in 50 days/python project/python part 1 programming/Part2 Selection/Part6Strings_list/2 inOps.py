cName = "Python"

userSearch = input("Enter course to search for : ").title()



if userSearch in cName:

    print(f"Found {userSearch}")

else:

    print(f"Not found {userSearch}")

    name = "Jane Smith"

vowels = ["a","e", "i", "o","u"]



for x in vowels: # x = "a","e", "i", "o","u"

    if x in name:

        print(x)

    else:

        print(f"Not found {x}")

      
      for x in vowels:  # x = "a","e", "i", "o","u"

    if x in name:

        print(x)

        break  # exit the loop once the first vowel is found

    else:

        print(f"Not found {x}")
