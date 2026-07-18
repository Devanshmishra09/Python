# swaping of two numbers :
# 1
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
a,b=b,a
print(a,b)

# 2
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a
a=b
b=c
print(a,b)

#addition of numbers
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a+b   
print(c)    

#subtraction of numbers
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a-b       
print(c)    

#multiplication of numbers
a=int(input("Enter the number :"))  
b=int(input("Enter the number :"))
c=a*b
print(c)

#division of numbers
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a/b
print(c)

#modulus of numbers
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a%b
print(c)

#exponent of numbers
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a**b
print(c)

#floor division of numbers
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=a//b
print(c)

#factorial of numbers
import math
a=int(input("Enter the number :"))
c=math.factorial(a)
print(c)    

#fibonacci series of numbers
a=int(input("Enter the number :"))
b=0
c=1
print(b,c,end=" ")
for i in range(2,a):
    d=b+c
    print(d,end=" ")
    b=c
    c=d
