# Q 1 Swap keys and values in a dictionary
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
swapped_dict = {value: key for key, value in a.items()}
print(swapped_dict)


# Q 2 Find the sum of all values in a dictionary.
a={"John":85,"Alice":90,"Bob":78,"Eve":92}
total_sum = sum(a.values())
print(total_sum)

# Q 3 Print numbers from 1 to 100.
for i in range (0,100):
    i=i+1
    print(i)
    
    
# Q 4 Print numbers from 100 to 1
a=101
for i in range(a):
    i=100-i
    print(i)


# Q 5 Print the multiplication table of a given number.
a=int(input(" enter the number"))
for i in range(1,11):
    i=a*i
    print(a,"*",i,"=",i)
    

# Q 6 Print the multiplication table .
for i in range(1,20):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("\n")
    

# Q 7 Find the factorial of a number.
a=int(input(" enter the number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
    print(fact)
    
# Q 8 Check whether a number is prime

a=int(input(" enter the number"))
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")
        
        
# Q 9 Print the Fibonacci series up to n terms

n=int(input(" enter the number of terms"))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
    print()  # Move to the next line after printing the series

# Q 10 Count vowels and consonants in a string
a=input(" enter the string")
vowels = 0
consonants = 0
for char in a:
    if char in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)


