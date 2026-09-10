# 1. Square of Numbers
# Given a list of numbers, use "map()" and "lambda" to create a new list containing the square of each number.

# numbers = [2, 4, 6, 8, 10]


lst=[2, 4, 6, 8, 10]
print(lst)
var=list(map(lambda a:a*a,lst))
print(var)

# 2. Add 10 to Each Number
# Use "map()" and "lambda" to add "10" to every element of the list.

# numbers = [5, 10, 15, 20, 25]

lst=[5, 10, 15, 20, 25]
print(lst)
var=list(map(lambda x:x+10,lst))
print(var)

# 3. Convert to Uppercase
# Given a list of names, use "map()" and "lambda" to convert every name to uppercase.

# 3. Convert to Uppercase
# Given a list of names, use "map()" and "lambda" to convert every name to uppercase.

# # names = ["suraj", "rahul", "amit", "rohit"]

names =["suraj","rahul","amit","rohit"]
print(names)
var=list(map(lambda a:a.upper(),names))
print(var)

# 4. Find Length of Each String
# Use "map()" and "lambda" to find the length of every string in the list.

# words = ["Python", "Java", "JavaScript", "C++"]

lst=["Python", "Java", "JavaScript", "C++"]
print(lst)
var=list(map(lambda a:len(a),lst))
print(var)


# 5. Convert Celsius to Fahrenheit
# Use "map()" and "lambda" to convert each temperature from Celsius to Fahrenheit.

# Formula:

# F = (C × 9/5) + 32

# celsius = [0, 10, 20, 30, 40]

lst= [0, 10, 20, 30, 40]
print(lst)
var=list(map(lambda a:(a*9/5)+32,lst))
print(var)

# 6. Find Even Numbers
# Use "filter()" and "lambda" to extract all even numbers from the list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
var=list(filter(lambda x:x%2==0,lst))
print(var)

# 7. Find Numbers Greater Than 10
# Use "filter()" and "lambda" to extract numbers greater than "10".

# numbers = [5, 12, 8, 20, 15, 3, 25]

lst= [5, 12, 8, 20, 15, 3, 25]
print(lst)
var=list(filter(lambda x:x>10,lst))
print(var)


# 8. Find Positive Numbers
# Use "filter()" and "lambda" to extract only positive numbers.

# numbers = [-10, 5, -3, 8, 0, -7, 12]

lst= [-10, 5, -3, 8, 0, -7, 12]
print(lst)
var=list(filter(lambda x:x>0,lst))
print(var)



# 9. Find Names Starting with "A"
# Use "filter()" and "lambda" to find all names that start with the letter ""A"".

# names = ["Amit", "Rahul", "Ankit", "Suraj", "Anjali", "Rohit"]

lst=["Amit", "Rahul", "Ankit", "Suraj", "Anjali", "Rohit"]
print(lst)
var=list(filter(lambda x:x[0]=="A",lst))
print(var)


# 10. Find Numbers Divisible by 5
# Use "filter()" and "lambda" to find all numbers that are divisible by "5".

# numbers = [10, 12, 15, 18, 20, 23, 25, 30]


lst=[10, 12, 15, 18, 20, 23, 25, 30]
print(lst)
var=list(filter(lambda a:a%5==0,lst))
print(var)



# 11. Find the Sum of All Numbers
# Use "reduce()" and "lambda" to calculate the sum of all numbers in the list.

# numbers = [10, 20, 30, 40, 50]

from functools import*
lst= [10, 20, 30, 40, 50]
print(lst)
var=int(reduce(lambda x,y:x+y,lst))
print(var)

# 12. Find the Product of All Numbers
# Use "reduce()" and "lambda" to calculate the product of all numbers.

# numbers = [2, 3, 4, 5]
from functools import*
lst= [2, 3, 4, 5]
print(lst)
var=int(reduce(lambda x,y:x*y,lst))
print(var)


# 13. Find the Maximum Number
# Use "reduce()" and "lambda" to find the largest number in the list.

# numbers = [12, 45, 7, 89, 23, 56]

from functools import*
lst= [12, 45, 7, 89, 23, 56]
var=int(reduce(lambda a,b:a if a>b else b,lst))
print(var)


# 14. Square Only Even Numbers
# Given a list of numbers:

# 1. Use "filter()" and "lambda" to select even numbers.
# 2. Use "map()" and "lambda" to calculate their squares.
# 3. Print the final list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
var=list(filter(lambda x:x%2==0,lst ))
var1=list(map(lambda x:x*x,var))
print(var)
print(var1)


# 15. Sum of Squares of Even Numbers
# Given a list of numbers:

# 1. Use "filter()" and "lambda" to select even numbers.
# 2. Use "map()" and "lambda" to calculate their squares.
# 3. Use "reduce()" and "lambda" to calculate the sum of those squares.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Topics Covered

# - "lambda"
# - "map()"
# - "filter()"
# - "reduce()"
# - Combining "map()" + "filter()"
# - Combining "map()" + "filter()" + "reduce()"
from functools import*
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
var=list(filter(lambda x:x%2==0,lst))
var1=list(map(lambda x:x*x,var))
var2=int(reduce(lambda x,y:x+y,var1))
print(var)
print(var1)
print(var2)
