# check you can vote or not
age=28
if age>=18:
    print("you can vote")

num=23
if num%2==0:
    print("even number")
else:
    print("odd number")
#  markss question
marks=72
if marks>90:
    print("A+")
elif  marks>80:
    print("A")
elif marks>70:
    print("b+")
elif marks>60:
    print("b")
elif marks>50:
    print("c+")
elif marks>40:
    print("c")
else:
    print("fail")

a=2399
b=567
c=78
if a>b and a>c:
    print("a is greater number")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

# age
age=int(input(" enter a age"))
if (age>18):
    voterid=input("enter your voteridid yes/no")
    if (voterid=="yes"):
        print("you can vote")
    else:
        print("you cannot vote first created voterid")
else:
    print("you cannot vote because you are under age")

# leap year question
year=int(input("enter a year"))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")

# check even number without using if-else statement
for i in range(2,101,2):
    print(i)

# print table
a=int(input("enter a number"))

for j in range(1,11):
        print(a,"*",j,"=",a*j)

# while loop year
i=1
while i<=10:
    print(i)
    i=i+1


a=int(input("enter a number"))
for i in range(1,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)


a=int(input("enter a number"))
count=0
if (a<=1):
    count=count+1
else:
    for i in range(2,a):
        if (a%i==0):
            count=count+1
if count==0:
    print("prime")
else:
    print("not prime")

# use break
for i in range(1,20):
      print(i)
      if i==15:
        break

for i in range(1,1):




