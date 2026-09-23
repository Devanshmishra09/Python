# NAN function : Not a number 
# it is commonly used to represent missing and undefined numericial values .
# gives true and false values 
# Is NaN : find nan values 
# ex 

import numpy as n 
aa=n.array([10,20,30,n.nan,40,50,n.nan])
c=n.isnan(aa)
print(c)

# NAN MEAN: Ignored nan value and find mean of the array :
# Ex 

import numpy as n 
aa=n.array([10,20,30,n.nan,40,50,n.nan])
c=n.nanmean(aa)
print(c)

# NAN MEDIAN : ignored nan value and find median value :
# Ex

import numpy as n 
aa=n.array([10,20,30,n.nan,40,50,n.nan])
c=n.nanmedian(aa)
print(c)

# NAN MNIMUM : Ignored nan values and gives minimum values :
# Ex 
import numpy as n 
aa=n.array([10,20,30,n.nan,40,50,n.nan])
c=n.nanmin(aa)
print(c)

# NAN MAXIMUM : Ignored nan value and gives maximum values .
# Ex 

import numpy as n 
aa=n.array([10,20,30,n.nan,40,50,n.nan])
c=n.nanmax(aa)
print(c)

# 