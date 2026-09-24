#    COPY AND VIEW 
# 
# Copy : in copy  it can assign value it can not be changed .
# and it can not  be create any other array .

# ex 

import numpy as n 
a=n.array([10,20,54,21,63,87,21])
b=a.copy()
b[5]=456
print(a)
print(b)

# View : In view we can assign value it can be changed . 
# And it can not be created anyother array .
# Ex 

import numpy as n 
a=n.array([10,20,54,21,63,87,21])
b=a.view()
b[5]=456
print(a)
print(b)

# n. shares_memory : it checks the share reference of view and copy . 
# it gives True and false values 
# ex 
# for view 
import numpy as n 
a=n.array([10,20,54,21,63,87,21])
b=a.view()
b[5]=456
print(n.shares_memory(a,b))
print(a)
print(b)


# for copy 
import numpy as n 
a=n.array([10,20,54,21,63,87,21])
b=a.copy()
b[5]=456
print(n.shares_memory(a,b))
print(a)
print(b)