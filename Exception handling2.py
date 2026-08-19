#question6->. Login System

#Create a simple login system.

#Use:
#username = "admin"
#password = "python123"

#Take username and password from the user.

#Requirements:
#- If the username or password is incorrect, use raise to generate an exception.
#- Handle the exception using try-except.
#- If both are correct, print "Login Successful".
#- Display an appropriate error message for invalid login.

user_name="Devansh"
password1=181818

try:
    username=str(input("enter a name"))
    password=int(input("enter a password"))
    if user_name!=username or password1!=password:
        raise Exception("error,username or password is incorrect")
    print("login successful")
except Exception as f:
    print("invalid",f)

#question7->. Custom Exception for Age

#Create a custom exception named AgeError.

#Requirements:
#- Create AgeError by inheriting from Exception.
#- Take age from the user.
#- If age is less than 18, raise AgeError with the message "Age must be 18 or above".
#- Handle AgeError using try-except.
#- If the age is valid, print "You are eligible"

class AgeError(Exception):
   pass

try:
    age=int(input("enter a age"))
    if age<18:
      raise AgeError("Age must be 18 or above")
    print("you are eligible")
        
   
except AgeError as f:
    print(f)


#question8->. Custom Exception for Insufficient Balance


#Create a custom exception named InsufficientBalanceError.

#Requirements:
#- Set balance = 5000.
#- Take withdrawal amount from the user.
#- If withdrawal amount is greater than balance, raise InsufficientBalanceError.
#- Handle the custom exception using try-except.
#- If the transaction is successful, display the remaining balance.


class InsufficientBalance(Exception):
    pass
Balance=5000
try:
    amount=int(input("enter a amount"))
    if Balance<amount:
     raise InsufficientBalance("Insufficient Balance Error")
    Balance=Balance-amount
    print("transaction is successful")
    print(Balance)
except InsufficientBalance as f:
   print(f)
except ValueError:
   print("error please enter amount")