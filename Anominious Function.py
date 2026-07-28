# Anominious  function: Defind Without Name 
# eg 

var=lambda a,b: a+b
print(var(10,20))

# greater of two numbers :
var=lambda a,b: (a,"a is greater than b") if a>b else (b,"b is greater than a ")
print(var(50,87))

# Filter Function : is used to filter the functions
def add(n):
    return n%2==0
lst=[50,20,74,77,695,59,35484,547,543,43543,46477,4174,44,55,49,58]
print(list(filter(add,lst)))


# prime series : 
def add(n):
    if n<2 :
        return False
    for i in range (2,n):
        if i % 2==0:
            return False
        return True
    lst=[97,79,13,11,25,48,3,7,85,38,38,245,685,38]
    print(list(filter(add,lst)))
    
    
# map function : performs operators on each sequence:
lst=[456,2,48,258,6398,2,8,658,4,87,689,4,73,742,5]
def add(n):
    return n+10
print(list(map(add,lst)))

# map using lambda :
d="DEVANSH"
print(list(map(lambda d:d.lower(),d)))


# reduce function :
from functools import*
Salary=[10000,20000,30000,40000]
print(reduce(lambda x,y :x+y,Salary))