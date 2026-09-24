#  Joining & Splitting Arrays 
# Joining combines arrays into a larger array. 
# Splitting divides one array into several arrays.
# Axis matters because a 2D array can be combined vertically or horizontally.

# concatenate() Joins along an existing axis. — stack()
#vstack() Vertical combination. — hstack() split() 
# Splits into equal sections when possible. — array_split()

# np.concatenate() Join along an existing axis. np.concatenate((a,b),axis=0) 

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
b=n.array([[10,30,50],[20,40,60]])
c=n.concatenate((a,b),axis=0)
print(c)

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
b=n.array([[10,30,50],[20,40,60]])
c=n.concatenate((a,b),axis=1)
print(c)

# np.stack() Join using a new axis. np.stack((a,b),axis=0) 

import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
b=n.array([[10,30,50],[20,40,60]])
c=n.concatenate((a,b),axis=0)
print(c)


import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
b=n.array([[10,30,50],[20,40,60]])
c=n.concatenate((a,b),axis=1)
print(c)

