import logging

import time

# set logging level

logging.basicConfig( filename=r"Part8 Lambdas_Exception\2 Exceptions\file2.log" , level=logging.DEBUG)




try:

    num1 = 10 #int(input("Enter a number: "))

    num2 = 0

    answer = num1 / num2

    print(f"The answer to {num1} / {num2}:  {answer}")

    logging.info(f"On {time.asctime()}\nDivision in progress {num1} / {num2}:  {answer}")

except ZeroDivisionError:

    print("You can't divide by zero")

    logging.error(f"On {time.asctime()}\nUser attempted to divide a number by zero")

finally:

    print("closing")