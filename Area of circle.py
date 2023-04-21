# Wirte a program to print the area of a circle.

# Solution :

# Formul for area of circle is = pi*r**2. Here pi = 3.14159 is a contant value in mathematics and r = radius of circle

# Import math module for constant value of pi.

import math

# Promt the user to input the value of radius and conver it into float()

radius = float(input("Enter radius value :"))

# Calculate the area by using circle formula & store the value into the area variable.

area = math.pi*radius**2

# Finally print the area of the circle with a proper format.

print(f"Area of the circle is :{area:.1f}")
