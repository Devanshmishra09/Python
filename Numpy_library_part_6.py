# Broadcasting : It allows numpy to perform element wise operations . 
# When two array are not equal it performs and equal them .

# Ex 

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
b=n.array([[20]])
c=a+b
print(c)

# # UNIVERSAL FUNCTION :
# A ufunc is a numpy function designled ti=o operate element by element .
# Ufunc are a key part of vectorizatiom numerical programing .

# Square root : Use to find square root 

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
print(n.sqrt(a))

# Square : use to find square of array 
 
import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
print(n.square(a))

# Exponantial value : to find exponantial value ;

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
print(n.exp(a))

# Natural lagorithim : used to find lagorithim 

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
print(n.log(a))

# log10 : used to find the base to log10 

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
print(n.log10(a))

# sin/cos/tan: used to find trigonometric function .

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
print(n.sin(a))
print(n.cos(a))
print(n.tan(a))

