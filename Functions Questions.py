 # Q 1 Use map() with a simple function to find the square of every number in a list.

lst=[2,3,4,5,6,7,8,9,10]
def a(n):
    return n*n
print(list(map(a,lst)))


# Q 2 Use map() with a lambda function to add 10 to every number in a list.

lst=[10,20,30,40,50,60,70,80,90,100]
print(list(map(lambda n:n+10,lst)))


# Q 3 Use map() with a lambda function to convert all names to uppercase.

lst=["devansh","shubh","shivansh","suraj"]
print(list(map(lambda n:n.upper(),lst)))


# Q 4 Use filter() with a simple function to find all even numbers from a list.

lst=[2,4,5,6,8,7,1,3,9,13]
def a(n):
    return n%2==0
print(list(filter(a,lst)))


# Q 5 Use filter() with a lambda function to find all odd numbers from a list.

lst=[2,4,5,6,8,7,1,3,9,13]
print(list(filter(lambda n: n%2!=0,lst)))


# Q 6 Use filter() with a lambda function to find all numbers greater than 30.

lst=[20,45,87,23,31,29,65,15,48,13,56,24,16]
print(list(filter(lambda n:n>30,lst)))


# Q 7 Use reduce() with a lambda function to find the sum of all numbers in a list.

from functools import*
lst=[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,lst))

# Q 8 Use reduce() with a simple function to find the largest number in a list.

from functools import*
lst=[52,4,69,36,487,68,38,6,866,86]
def a(x,y):
    return x if x>y else y
print(reduce(a,lst))

