# This is variable has a global scope and accessible from anywhere in the program

globalNum1 = 5




def localSubRoutine():

    print(f"Printing global variable {globalNum1} from localSubRoutine")

    localNum1 = 10

    print(f"Printing local variable {localNum1} from localSubRoutine")




localSubRoutine()



print(f"Printing global variable {globalNum1} from global")

def modifyGlobalNum():

    global globalNum1 # use globa keyword to modify the value held in globalNum1 variable

    globalNum1 = 500

    print(f"Printing modified global variable {globalNum1} from localSubRoutine")

modifyGlobalNum()

print(f"Printing global variable {globalNum1} from global?????")