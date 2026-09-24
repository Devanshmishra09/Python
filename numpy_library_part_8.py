# np.vstack() Vertical stack. np.vstack((a,b))

import numpy as n 
a=n.array([[10,20,30],[70,80,90]])
b=n.array([[40,50,60],[33,44,55]])
c=n.vstack((a,b))
print(c)

# for 1 dimension 
import numpy as n 
a=n.array([10,20,30])
b=n.array([40,50,60])
c=n.vstack((a,b))
print(c)


# np.hstack() Horizontal stack. np.hstack((a,b))
import numpy as n 
a=n.array([[10,20,30],[70,80,90]])
b=n.array([[40,50,60],[33,44,55]])
c=n.hstack((a,b))
print(c)

# for 1 dimension array 

import numpy as n 
a=n.array([10,20,30])
b=n.array([40,50,60])
c=n.hstack((a,b))
print(c)


