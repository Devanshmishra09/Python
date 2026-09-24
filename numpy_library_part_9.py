# np.array_split() Flexible split. np.array_split(arr,3) 
# split method 

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70])
c = np.split(arr, [5, 2])
print(c)


# np.vsplit() Vertical split. np.vsplit(arr,2) 
# it wrks on 2d or more than 2d 


import numpy as np
arr = np.array([[10, 20, 30, 55],[40, 50, 60, 70]])
c = np.vsplit(arr, [5])
print(c)

# np.hsplit() Horizontal split. np.hsplit(arr,2)
import numpy as np
arr = np.array([[10, 20, 30, 55],[40, 50, 60, 70]])
c = np.hsplit(arr, [5])
print(c)
