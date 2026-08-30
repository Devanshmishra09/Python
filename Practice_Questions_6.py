# Write a function in prime number to check number os prime or not :

a=int(input("Enter the number :"))
count=0
if a<=1 :
    count=1
else :
    for i in range(2,a):
        if(a%i==0):
            count=count+1
if count==0:
    print("number is prime ")
else:
    print("number is not prime")
    
    
# factorial of a number

a=int(input("Enter the number : "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)


# Student Marks and Grade
# Write a function calculate_result(marks) that takes a list of marks and calculates:

# Total marks
# Percentage
# Grade
def calculate_result(marks):
    total=0
    for num in marks:
        total=total+num
    Percentage=total/5
   
    if Percentage>=90 and  Percentage<=100:
        print("A Grade")
    elif Percentage>=80 and Percentage<=90:
        print("B Grade")
    elif Percentage>=70 and Percentage<=80:
        print("c Grade")
    elif Percentage>=60 and Percentage<=70:
        print("d Grade")
    elif Percentage>=50 and Percentage<=60:
        print("E GRade")
    else:
        print("Fail")
    return Percentage,total
marks=(95,86,98,76,96)
print(calculate_result(marks))

# Fibonacci Series
# Write a function fibonacci(n) that returns the first n terms of the Fibonacci series
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
fibonacci(18)


# Reverse a String
# Write a function reverse_string(text) that reverses a string without using [::-1].
def reverse_string(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev
print(reverse_string("shivam"))


# Count Vowels
# Write a function count_vowels(text) that counts the number of vowels in a given string. 
# The function should handle both uppercase and lowercase letters.
def count_vowels(text):
    count=0
    for ch in text:
        if ch.lower() in "aieou":
            count+=1
    return count
text=input("enter a text")
print(count_vowels(text))