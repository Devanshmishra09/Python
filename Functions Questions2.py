# Q 1 Use map() with a lambda function to find the cube of every number in a list.

lst=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda n:n**3,lst)))

# Q 2 Use filter() with a lambda function to find all positive numbers from a list.

lst=[1,-2,3,4,-5,-6,-7,5,8,15,6,-8,-9,-48]
print(list(filter(lambda n:n>0,lst)))

# Q 3 Use filter() with a simple function to find all prime numbers from a list.


def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        i%2==0
        return False
    return True
lst=[1,3,2,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(list(filter(prime,lst)))

# Q 4 Use filter() with a lambda function to find all words whose length is greater than 5.

lst=["DEVANSH","SHUBH","SURAJ","SHIVAM","SHIVANSH","SURYANSH","VEDANSH"]
print(list(filter(lambda x:len(x)>5,lst)))

# Q 5 Use map() with a simple function to convert temperatures from Celsius to Fahrenheit.

lst=[30,50,21,54,55,8,98,4,54,65]
def cel(n):
    return (n*9/5)+32
print(list(map(cel,lst)))


# Q 6 Use map() with a lambda function to convert all integers into strings.

lst=[4,5,8,7,9,6,5,9,59,56,5,5]
print(list(map(lambda n:str(n),lst)))


# Q 7 Use reduce() with a lambda function to find the product of all numbers in a list.

from functools import*
lst=[6,5,8,4,4,76,2,4,67,24,24,24,2]
print(reduce(lambda x,y:x*y,lst))

# Q 8 Use filter() with a lambda function to find all words that start with a vowel.

lst=["DEVANSH","SHIVANSH","SHUBH","VEDANSH","ARYA","ISHA"]
print(list(filter(lambda x: x and x[0].lower() in 'aeiou',lst)))


# Q 9 Use map() with a simple function to find the factorial of every number in a list.
from math import*
lst=[1,2,3,4,5,6,7,8,9,10]
def fact(x):
    return factorial(x)
print(list(map(fact,lst)))

