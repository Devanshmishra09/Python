# numpy is designed for numerical callculation,scientific computing it provides a powerful multidimensional
#array object along with function for static calculation and operation .

# ex 1

import numpy as N
num=N.array([10,20,30,40,50])
r=num+10
print(r)
print(type(num))

# Numpy performson each element on array is called Vectorization.

# Types of Array 
# 1. dimensional array :
#           a one dimensional array is similar to single row array .

# ex

import numpy as N
num=N.array([10,20,30,40])
print(num.ndim)

# 2. Dimensional array :
#        A two dimensional array is contain row and column :
#   Ex 

import numpy as n
num=n.array([[10,20,30,40],[10,20,30,40]])
print(num.ndim)


# 3. Dimensional array :
#     A three dimensional contains multiple two dimensional array .
#   Ex 

import numpy as n
num=n.array([[[10,20,30,40],[10,20,30,40],
             [50,60,70,80],[90,80,70,60],
             [40,50,60,70],[40,20,30,10],
             [70,80,90,50],[47,55,47,58]]])
print(num.ndim)


# Defines how many row and collumn in a array :
 
#   Ex 
import numpy as n 
num=n.array([[10,20,30,40],[10,20,30,50]])
print(num.shape)


#  Attributes : Represent the property and information of array.

# size = Defines number of elements 
# shape = defines Row and collumn of array 
# ndim = show the dimension of array
# itemsize = showes the size of item in bytes 
# dtype = Showes the type of array 
# nbytes = show the size to total array 
# T = (Tranpose) means convert row into collums and collumn into row 

#  Ex 
import numpy as n 
num=n.array([[10,20,30,40],[1,20,30,40]])
print(num.shape)
print(num.size)
print(num.ndim)
print(num.itemsize)
print(num.dtype)
print(num.nbytes)
print(num.T)    

