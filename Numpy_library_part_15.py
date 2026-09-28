#  Linear algebra 
# Linear algebra is important in machine learning statics and numerical modeling.
# numpy module provides matrix operations suh as solving systems calculation determation elgenvalues norms and rank .

# dot product : it means multiple of sets .
# when the column of 1 set is equal to the row of second sets 

# ex

import numpy as n 
a=n.array([10,20,30,40,50]) 
b=n.array([10,20,30,40,50]) 
print(n.dot(a,b))


# for 2 dimension

import numpy as n 
a=n.array([[10,20,30],[40,50,60]]) 
b=n.array([[10,20,30],[40,50,60],[70,80,90]]) 
print(n.dot(a,b))
