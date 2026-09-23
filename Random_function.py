# random Function :
# Generate random values 

# random.random(): use to generate floating value from 0 to 1 :

import numpy as n 
a=n.random.random(5) 
print(a)

# random.randint(): it is used to generate integer value .(start,end,no of times )

import numpy as n 
a=n.random.randint(10,35,10)
print(a)

# random.randn(): it generates negative and positive random floating numbers .

import numpy as n 
a=n.random.randn(5)
print(a)

#  Choice : it generates random value from given 1 dimensional array .

import numpy as n 
a=n.array([10,20,30,40,50,60])
b=n.random.choice(a)
print(b)

# for 2 dimensional array : we use flattent 
import numpy as n 
a=n.array([[10,20,30],[40,50,60]])
b=n.random.choice(a.flatten())
print(b)