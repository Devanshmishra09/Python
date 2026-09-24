# Searching & indexing 
 # n.argmax: Giving maximum indexing behalf of max element 
 
import numpy as n 
a=n.array([10,20,304,50,806,0,4050,80])
c=n.argmax(a)
print(c)


# n.argmin : giving minum index behalf of minimum  elements 

import numpy as n 
a=n.array([10,5880,690,58,5,8,8,63,9085,5,69,58])
c=n.argmin(a)
print(c)


# n.searchsorted : it tells us that at which place our value can be added .
#  it means at which index value .

import numpy as n 
a=n.array([18,52,8269,2,96,2,2,6,2,6258,2,2826,2,25,2,5,56])
c=n.searchsorted(a,4826)
print(c)

# for 2 dimensional array :

import numpy as n 
a=n.array([[15,22,26],[58,69,33]])
c=n.searchsorted(a[1],45)
print(c )