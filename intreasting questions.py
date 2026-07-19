# write a progran in python to print simple interest
# simple interest formula: SI = (P * R * T) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)




# write a program in python to print compound interest
# compound interest formula: CI = P * (1 + R/100)^T - P

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
compound_interest = principal * (1 + rate/100) ** time - principal
print("The compound interest is:", compound_interest)   


# write a program in python to print area of circle
# area of circle formula: A = π * r^2

import math
radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
print("The area of the circle is:", area_of_circle)


#circumference of circle formula: C = 2 * π * r

radius = float(input("Enter the radius of the circle: "))
circumference_of_circle = 2 * math.pi * radius
print("The circumference of the circle is:", circumference_of_circle)



# write a program in python to print area of rectangle
# area of rectangle formula: A = l * w
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_of_rectangle = length * width
print("The area of the rectangle is:", area_of_rectangle)

# write a program in python to print area of square
# area of square formula: A = a^2
side = float(input("Enter the side of the square: "))
area_of_square = side ** 2
print("The area of the square is:", area_of_square)


# write a program in python to print area of triangle
# area of triangle formula: A = (b * h) / 2


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_of_triangle = (base * height) / 2
print("The area of the triangle is:", area_of_triangle)


#circumference of circle formula: C = 2 * π * r

radius = float(input("Enter the radius of the circle: "))
circumference_of_circle = 2 * math.pi * radius
print("The circumference of the circle is:", circumference_of_circle)


#time conversion in python
# 1 hour = 60 minutes
# 1 minute = 60 seconds
# 1 day = 24 hours

hours = int(input("Enter the number of hours: "))
minutes = hours * 60
seconds = minutes * 60
print(f"{hours} hours is equal to {minutes} minutes and {seconds} seconds.")

minutes = int(input("Enter the number of minutes: "))
hours = minutes / 60
seconds = minutes * 60
print(f"{minutes} minutes is equal to {hours} hours and {seconds} seconds.")


seconds = int(input("Enter the number of seconds: "))
hours = seconds / 3600
minutes = seconds / 60
print(f"{seconds} seconds is equal to {hours} hours and {minutes} minutes.")

days = int(input("Enter the number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"{days} days is equal to {hours} hours, {minutes} minutes and {seconds} seconds.")

