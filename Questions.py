#question1-> Safe Division Calculator

#Write a Python program that takes two numbers from the user and performs division.

#Requirements:
#- Use try-except.
#- Handle ValueError if the user enters a non-numeric value.
#- Handle ZeroDivisionError if the second number is 0.
#- Print a suitable error message for each exception.


try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a/b)
except ValueError:
    print("error,please enter numeric value")
except ZeroDivisionError:
    print("error,not possible divide by zero")


#question2-> Student Marks Validator

#Write a program that takes marks from the user.

#Requirements:
#- Marks must be between 0 and 100.
#- If the user enters a non-numeric value, handle ValueError.
#- If marks are less than 0 or greater than 100, use raise to generate a ValueError.
#- Display a suitable message for invalid marks.

#method1
try:
   marks=int(input("enter a marks"))
   if marks<0 or marks>100:
      raise ValueError("error,enter a marks between 0 to 100")
   print(marks)
except ValueError as f:
   print(f)


#method2

try:
   marks=float(input("enter a marks"))
   if marks<0 or marks>100:
      raise ValueError("error,enter a marks between 0 to 100")
   print(marks)
except ValueError as e:
   print("error,enter a numeric value",e)


#question3->. Bank Withdrawal System

#Create a simple bank withdrawal program.

#Requirements:
#- Set an account balance of ₹10,000.
#- Take the withdrawal amount from the user.
#- If the amount is greater than the balance, use raise to generate an Exception.
#- Handle the exception using try-except.
#- If the withdrawal is successful, display the remaining balance.

balance=10000
try:
    amount=int(input("enter a amount"))
    if amount>balance:
     raise Exception("Insufficient balance")
    balance=balance-amount
    print("withdrawal successfully")
    print(balance)
except Exception as e:
    print("error",e)
    

#4. Age Eligibility Checker

#Write a program that takes a person's age.

#Requirements:
#- Convert the input into an integer.
#- Handle ValueError if the user enters invalid data.
#- If the age is less than 18, use raise to generate an exception with the message "Not eligible".
#- If the age is 18 or above, print "Eligible".


try:
    age=int(input("enter a age"))
    if age<18:
        raise Exception("error,not eligible")
        
    print("eligible")

except ValueError:
    print("error,enter a valid age")

except Exception as f:
   print(f)



#question5->. File Handling with Exception Handling

#Write a program to read data from a file named "student.txt".

#Requirements:
#- Use try-except-finally.
#- Handle FileNotFoundError if the file does not exist.
#- If the file exists, print its contents.
#- Use finally to print "File operation completed".


try:
    with open("student.txt","r")as f:
        print(f.read())
except FileNotFoundError:
    print("error,file does not exist")
finally:
    print("File operation completed")