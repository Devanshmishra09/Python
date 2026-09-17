# using methpd in numpy .
# reshape
# resize 
# Flattent 
# sum 
# mean 
# average 
# median 
# mode  
# min 
#  max

# Reshape : chang the shape of row and collumns 
import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
a.reshape(2,3)
print(a)

# Resize : when row and collumns are not equal it  could contain zero when it is less otherwise
# it could remove the values .
import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
v=a.resize(3,2)
print(v)

# flattent 
# convert multi dimensional array into a single row 
import numpy as n 
a=n.array([[10,20,30],[10,20,30]])
v=a.flatten()
print(v)

# sum : sum all the elements 
import numpy as n 
a=n.array([[10,20,30],[10,20,30]])
v=a.sum()
print(v)

# mean : gives average of lists 
import numpy as n 
a=n.array([[10,20,30],[10,20,30]])
v=a.mean()
print(v)

# mode : gives highest no of frequency in lists 
import numpy as n 
from scipy import stats
a=n.array([[10,20,30],[10,20,30]])
v=stats.mode(a)
print(v)

# median : gives median of a list 
import numpy as n 
a=n.array([[10,20,30],[10,20,30]])
v=n.median(a)
print(v)
# odd 
import numpy as n 
a=n.array([[10,20,30,10,20,30]])
v=n.median(a)
print(v)

# standard Derivation : 
import numpy as n 
a=n.array([[10,20,30],[10,20,30]])
v=n.std(a)
print(v)

# min/ max 
import numpy as n 
a=n.array([[10,20,30],[10,20,30]])
v=a.min()
print(v)
c=a.max()
print(c)