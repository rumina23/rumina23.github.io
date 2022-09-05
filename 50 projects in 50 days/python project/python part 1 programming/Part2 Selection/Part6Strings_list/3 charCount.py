searchStr = "Python is a great programming language cohort 11"

findChar = input("Enter character to search for ")

counter = 0  # the flag variable counter holds a value of 0




for aChar in searchStr:

    print(aChar)



    if aChar == findChar:

        "counter = 0 +1, counter = 1 + 1....."

        counter = counter + 1  # counter +=1

print(f"Found the character : {findChar} {counter} times")


def userSearcg():
  counter = 0
  for aChar in searchStr:
      if aChar == findChar:
         counter = counter + 1  # counter +=1
      print(f"Found the character : {findChar} {counter} times")

      userSearch()

     









