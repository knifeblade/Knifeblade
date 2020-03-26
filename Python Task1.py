# Python Task 1

title = "Basic Calculator for Area of a Circle"
print(title.upper())

# Python program which accepts radius of a circle from the user & computes area of the circle
# Area of circle = πr²; where π = 3.14159 and r = radius of circle
# Pi can be defined, or could be imported from Py module with 'from math import pi'

pi = 3.14159

radius = float(input("Please enter radius of the circle: "))
diameter = 2 * radius

print("The circle with a radius of " + str(radius) + " would also have a diameter of 2r = " + str(diameter))

Area = (pi * radius ** 2)

print("Area of the circle is: " + str(Area))
