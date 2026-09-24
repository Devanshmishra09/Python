# Vectorization : Performing operations on all the element of array is called vectorization :
#  vectorize method : in vectroize method it works like a function .

# ex 
# find even numbers from array using vectroize method 

import numpy as n 
a=n.array([10,450,60,58,5,6,26,2,3,28,21,23,27,4])
def even(a):
    if a%2==0:
        return a
    else:
        return 0
c=n.vectorize(even)
v=c(a)
v=v[v!=0] # we use this for removing zeros from array 
print(v)


# odd 

import numpy as n 
a=n.array([10,450,60,58,5,6,26,2,3,28,21,23,27,4])
def even(a):
    if a%2!=0:
        return a
    else:
        return 0
c=n.vectorize(even)
v=c(a)
v=v[v!=0] # we use this for removing zeros from array 
print(v)
