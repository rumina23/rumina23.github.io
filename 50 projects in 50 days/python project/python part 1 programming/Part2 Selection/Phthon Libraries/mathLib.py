import math  # import the math library/class/module

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2

print(f"The area is {area}")

print(f"The area displayed is rounded to 2 decimal places {area:.2f}")

print(f"The area displayed is rounded to 2 decimal places {area:.3f}")

# method 2

roundDown = math.floor(area)

print(f"The area is rounded down to the nearest whole number: {roundDown}")




# method 3

roundUp = math.ceil(area)

print(f"The area is rounded up to the nearest whole number: 345{roundUp}")

# method 4

print(f"Using the round method:{round(area,2)}")