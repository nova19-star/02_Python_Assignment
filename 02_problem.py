# 2. Write a python program to where three sides of triangle and display the perimeter and area 

import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
perimeter = a + b + c
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Perimeter:", perimeter)
print("Area:", round(area, 2))


