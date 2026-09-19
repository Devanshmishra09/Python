# 1 ARRAY CREATION METHOD 
# arange : with arange method we can create array from starting to ending with steping

# eg 
import numpy as n 
a=n.arange(1,200)
print(a)

# eg 2 : with stepping 
import numpy as n 
a=n.arange(1,200,5)
print(a)

# 2 linespace : difining how many elements you want from array . it give with equal difference

# eg 
import numpy as n 
a=n.linspace(1,200,15)
print(a)

# 3 Zeros : in this all elements are zero 
import numpy as n 
a=n.zeros(10)
print(a)

# 4 Random : it gives random value from starting to ending elements .

# eg 
import numpy as n 
a=n.random.randint(1,200,5)
print(a)

# eg for floating values 
import numpy as n 
a=n.random.rand(1,200,25)
print(a)


# ones : it gives all Ones 
#eg 
import numpy as n 
a=n.ones([1,2])
print(a)

# full : it gives no of elements in defind rows and columns 
# eg

import numpy as n 
a=n.full([2,5],10)
print(a)

