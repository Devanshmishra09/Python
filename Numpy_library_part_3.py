# numpy : boolean indexing and logicial operatiors 
# Boolean indexing filters array using true and false condition .
# it is most important techiniques without writing a loop .

# eg 
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
print(a[a>50])
print(a>50)


# for two logics 
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
print(a[(a>50)&(a<80)])

# using logical_and (operator)
import numpy as n 
a=n.array([[10,20,30],[40,50,60],[70,80,90]])
c=n.logical_and(a>50,a<80)
print(a[c])