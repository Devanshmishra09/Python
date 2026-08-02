# Function 

# Q 1 Write a function to check whether a number is even or odd
from functools import reduce


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(5))

 
# Q 2 Write a function to find the greatest of three numbers

def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greater(10,20,30))

# Q 3 Write a function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


# Q 4 Write a function to check whether a string is a palindrome.

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(palindrome("dad"))
print(palindrome("Hello"))
print(palindrome("eye"))


# Q 5  Write a function to return the sum and average of a list
def sum_and_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return total, average

print(sum_and_average([1, 2, 3, 4, 5]))


