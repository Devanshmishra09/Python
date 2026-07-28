# Function are block of code that perform specific tasks :
#typs :Predefind , Userdefind

# eg,
def add():
    a=10
    b=20
    print(a+b)
add()

# Parameters :

def add(a,b):
    print(a+b)
add(20,50)
add(60,40)

# Return statements :

def add(a,b):
    return a+b
print(add(50,40))

# if returns many values:
def b(num1,num2):
    a=num1+num2
    b=num1*num2
    c=num1/num2
    d=num1-num2
    return(a,b,c,d)
print(b(2,3))
print(b(20,4))

# Arguments 
# 1 positional arguments :
def add(a,b):
    print(a,b)
add(50,20)
add(20,70)

# keyword arguments :
def add(a,b):
    print("a is =",a, "b is =",b)
add(a=50,b=60)

# defalt argument :
def add(name="shivam"):
    print("hello",name,"how are you")
add()
add("Devansh")

# variable length argument :

def add(*n):
    add=0
    for i in n:
        add=add+i
    print(add)
add(20,30,50,10)


#  VARIABLES :
#LOCAL AND GLOBAL;

# Local Variables:
def a():
    a=10
    print(a)
a()

# Using local variable outside the function :

def add():
    global a;
    a=1000;
add()
print(a)


# Global variables :
a=10
def add():
    print(a)
add()

# recursive Functions:
def add(n):
    if n==0:
        return 
    print(n)
    add(n-1)
add(5)

# Factorial of anumber using Recursive:
def add(n):
    if n==0:
        return 1
    return n*add(n-1)
print(add(5))
