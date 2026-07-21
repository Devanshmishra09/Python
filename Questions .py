#  write a program to input two numbers and perform all arithmetic operations on them:

import math


a=int(input(" enter the first number :"))
b=int(input(" enter the second number :"))
print(" the sum is :",a+b)
print(" the difference is :",a-b)
print(" the product is :",a*b)
print(" the quotient is :",a/b)
print(" the modulus is :",a%b)
print(" the exponent is :",a**b)
print(" the floor division is :",a//b)
print(" the factorial of first number is :",math.factorial(a))



#  write a program to find reminder when two number is divided by each other:

a=int(input(" enter the first number :"))
b=int(input(" enter the second number :"))
x=float(a%b)
print(" the reminder is :",x)


#  write a program to calculate square and cube root of a number :


a=int(input(" enter the number :"))
print(" the square of the number is :",a**2)
print(" the cube of the number is :",a**3)
print(" the square root of the number is :",math.sqrt(a))
print(" the cube root of the number is :",a**(1/3))

# write a program to find greatest common divisor (GCD) and least common multiple (LCM) of two numbers:

a=int(input(" enter the first number :"))
b=int(input(" enter the second number :"))
print(" the GCD of the two numbers is :",math.gcd(a,b))
print(" the LCM of the two numbers is :",math.lcm(a,b))


# write a program to find the area of a triangle using Heron's formula:

a=float(input(" enter the first side of the triangle :"))
b=float(input(" enter the second side of the triangle :"))
c=float(input(" enter the third side of the triangle :"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" the area of the triangle is :",area)


# write a program to check a persion is eligible for voting or not:

age=int(input(" enter the age of the person :"))
if age>=18:
    print(" the person is eligible for voting ")
else:
    print(" the person is not eligible for voting ")
    
    
#  write a program of largest of three numbers:

a=int(input(" enter the first number :"))
b=int(input(" enter the second number :"))
c=int(input(" enter the third number :"))
if a>b and a>c:
    print(" the largest number is :",a)
elif b>a and b>c:
    print(" the largest number is :",b)
else:
    print(" the largest number is :",c)



# write a program to check whether a number is positive, negative or zero:

a=int(input(" enter the number :"))
if a>0:
    print(" the number is positive ")
elif a<0:
    print(" the number is negative ")
else:
    print(" the number is zero ")
    
    