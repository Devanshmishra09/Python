#question1> print a list
list="shubhsingh"
for i in list:
    print(i)

# print a table
a=int(input("enter a number"))
for i in range(1,11):
    print(i*a)

# find the factorial number
a=int(input("enter anumber"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

# find the sum number
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)

# find the sum of even number
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
        print(sum)

#  print the prime number or not
a=int(input("enter a number"))
count=0
if (a<=1):
    count=count=1
else:
    for i in range(2,a):
        if a%i==0:
            count=count=1
if count==0:
    print("prime")
else:
    print("not prime")

# sum of odd number
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
print(sum)

# given a string use a for loop to count how many vowels iaoue it contains
text=input("enter a number")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count=count+1
        print(count)

# reverse string
#  write a program to reverse a string using a for loop without using slicing
text=input("enter a letter")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print(rev)

#find the largest number
# given a list of number use a for loop to find the largest number in the list
number=[23,32,35,64,65,345,64]
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print(largest)