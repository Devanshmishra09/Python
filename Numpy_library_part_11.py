# Sorting : Finding index of array 
# first it converts accending order then gives its indexing behalf on acending order 
# use n.argsort()

import numpy as n 
a=n.array([10,20,30,40])
c=n.argsort(a)
print(c) 

# for 2 dimension 
import numpy as n 
a=n.array([[10,20,30,40],[70,80,90,85]])
c=n.argsort(a)
print(c) 

# For multi dimension
import numpy as n 
a=n.array([[[10,20,30,40],[45,46,78,95]],[[10,20,30,40],[70,80,90,85]]])
print(n.ndim(a))
c=n.argsort(a)
print(c) 