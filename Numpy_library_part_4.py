# logicial operator or

#ex 
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.logical_not(a>50,a<80)
print(a[c])

# logicial operator not 

# ex 
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.logical_not(a>50,a<80)
print(a[c])

# any : it returns true and false in single value will be true :

# ex 
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.any(a[a>50])
print(c)

# all : Check all the value are True or false :

# ex
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.all(a>50)
print(c)

# Where : it checks the conditions then returns output in form of indexing (row & columns):
# ex 

import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.where(a>50)
print(c)