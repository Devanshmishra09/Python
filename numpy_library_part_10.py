#  Insert, Delete, Append, Unique & Sorting 
# These functions are useful for small array transformations.
# Most of them return a new array instead of changing the original. 
# Repeated append/insert/delete operations can be expensive for very large numerical workflows.

# np.append() Adds values at the end and returns a new array. — arr.sort() 

import numpy as n 
a=n.array([10,20,30,40,50])
c=n.append(a,80)
print(c)


