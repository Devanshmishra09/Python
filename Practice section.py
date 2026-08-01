# q 1 Create a list of 10 numbers and print all elements.

a=[1,2,3,4,5,6,7,8,9,10]
print(a)

# Q 2 Print only even numbers from a list.

a=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2==0,a)))


# Q 3 Print only odd numbers from a list.

a=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2!=0,a)))


# Q 4 Find the largest element in a list without using max().
from functools import*
d=[1,5,4,8,7,10,9,3,5,6,8,6,3]
var=reduce(lambda a,b:a  if a > b else b,d)
print(var)

# Q 5 Find the smallest element in a list without using min().
from functools import*
d=[1,5,4,8,7,10,9,3,5,6,8,6,3]
var=reduce(lambda a,b:a  if a < b else b,d)
print(var)

# Q 6 Find the sum of all elements in a list.
from functools import*
d=[1,5,4,8,7,10,9,3,5,6,8,6,3]
print(reduce(lambda x,y:x+y,d))


# Q 7 Find the average of all elements in a list
from functools import*
d=[1,5,4,8,7,10,9,3,5,6,8,6,3]
print(reduce(lambda x,y:(x+y)/2,d))

# Q 8 Remove duplicate elements from a list.
d=[1,5,4,8,7,10,9,3,5,6,8,6,3]
print(set(d))

# Q 9 Reverse a list without using reverse()
a=[1,2,3,4,5,6,7,8,9,10]
b=a[::-1]
print(b)

# Q 10 Create a tuple and print all elements
a=(1,4,7,589,6,89,6,98,6,2,41,5,8,2,1,8,6,8,2,8,2,45)
print (type(a))
print(a)

# Q 11 Count the occurrence of an element in a tuple
a=(1,4,7,589,6,89,6,98,6,2,41,5,8,2,1,8,6,8,2,8,2,45)
print(a.count(2))

# Q 12 Find the index of a given element in a tuple
a=[1,2,3,4,5,6,7,8,9,10]
print(a.index(7))

# Q 13 Convert a tuple into a list and add a new element. 
a=[1,2,3,4,5,6,7,8,9,10]
print(type(a))

# Q 14 Find the maximum and minimum values in a tuple.
a=(1,4,7,589,6,89,6,98,6,2,41,5,8,2,1,8,6,8,2,8,2,45)
print(max(a))
print(min(a))

# Q 15 Create a set and print all elements
a={1,2,3,4,5,6,7,8,9,10}
print(a)

 