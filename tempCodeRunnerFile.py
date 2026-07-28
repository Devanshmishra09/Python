from functools import*
Salary=[10000,20000,30000,40000]
print(reduce(lambda x,y :x+y,Salary))