# Lambda Function
# Q 1 Use a lambda function to find the square of a number.
square = lambda x: x ** 2
print(square(5))


# Q 2 Use a lambda function to find the cube of a number

cube= lambda x: x ** 3
print(cube(3))


# Q 3 Sort a list of tuples based on the second element using a lambda function

a=[(1, 3), (2, 1), (4, 2), (3, 4)]
a.sort(key=lambda x: x[1])
print(a)    


# map(), filter(), reduce()
# Q 1 Use map() to find the square of every number in a lis.
 

a=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x**2,a)))


# Q 2 Use map() to convert a list of strings into uppercase

a=["devansh","shubh","shivansh","suraj"]
print(list(map(lambda x:x.upper(),a)))

# Q 3 Use filter() to find all even numbers from a list.

a=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,a)))

# Q 4 Use filter() to print all prime numbers from a list.

a=[2,3,4,5,6,7,8,9,10]
b= list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, a))
print(b)

# Q 5 Use reduce() to find the sum of all elements in a list.

from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,a))