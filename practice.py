# prime number program
# from user inputs 

a = int(input("Enter a number: "))
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")
        
        
# from 1 to 100 prime number program
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            
            
# from list of numbers prime number program
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            
# with lambda function prime number program
is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
    
    
# with function prime number program
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
    

# with recursion prime number program
def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

number = int(input("Enter a number: "))
if is_prime_recursive(number):
    print(number, "is a prime number")