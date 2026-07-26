# Random functions 

import random
secret=random.randint(1,10)
a=int(input("Enter any number from 1 to 10 :"))
while a!=secret:
    if a<secret:
        print("a is less than the secret number",secret)
    else:
        print("a is greater than the secret number",secret)
    a=int(input("Enter the number from 1 to 10 :"))
    print("congratuation you guess the exact number you won")
    


# loop Questions 
 
# ATM Balance System
# Ek program banao jisme initial balance ₹10000 ho. User se withdraw amount lo.
# Agar balance sufficient ho to amount deduct karo aur naya balance dikhao. 
# Har transaction ke baad pucho "Aur paisa nikalna hai? (yes/no)". 
# Jab tak user "yes" bole tab tak program chalta rahe.
    
  
Initial_balance=10000
while True:
    withdraw_amount=int(input("enter the amount you want to widthraw :")) 
    if withdraw_amount<=Initial_balance:
        amount=Initial_balance-withdraw_amount
        print("withdraw susscesfull ")
        print("Your remaining amount",amount)
    else:
        print("Insufficient balance",Initial_balance)
    choice=str(input("IF YOU WANT TO DO MORE TRANSACTION TYPE (YES) ELSE TYPE(NO) : "))
    if choice.upper()=="YES":
       continue
    else:
        print("thank you for transaction :")
        break
    

# Login System
# Ek program banao jisme username "admin" aur password "1234" ho. 
# User se username aur password tab tak input lo jab tak dono sahi na ho jaye. 
# Sahi hone par "Login Successful" print karo.


Name="Devansh Mishra"
password=123456
while True:
    User_Name=str(input("Enter the User name :"))
    User_Password=int(input("Enter the password :"))
    if Name==User_Name and password==User_Password:
        print("login susscesfull")
        break
    else:
        print("Please enter the valid user name and password")
        continue
    
    
    

#Student Marks Entry
# Ek program banao jisme har student ke marks input lo. Total aur average calculate karo.
# Har student ke baad pucho "Do you want to add another student? (yes/no)". 
# Jab tak user "yes" bole tab tak program chalta rahe.

while True:
    Student_Name=str(input("Enter the student name :"))
    English=int(input("enter the English marks :"))
    Maths=int(input("Enter the maths marks :"))
    Hindi=int(input("Enter the Hindi marks :"))
    Science=int(input("Enter the Science Marks :"))
    Social_Science=int(input("Enter the Social science marks :"))
    total_marks=English+Hindi+Science+Maths+Social_Science
    print("Your total marks is = ",total_marks)
    percentage=total_marks/5
    print("your percentage =",percentage)
    choice=str(input("IF YOU WANT TO FIND ANOTHER STUDENT TYPE (YES) ELSE TYPE (NO) "))
    if choice.upper()=="YES":
        continue
    else:
        print("thankyou for visiting ",Student_Name)
        break
    


#Shopping Bill Generator
# Ek program banao jisme product ka naam aur price input lo. Sabhi products ka total bill calculate karo. 
# Har product ke baad pucho "Add another product? (yes/no)". Jab user "no" bole tab final bill print karo.


Customer=str(input("Enter the customer name :"))
Total_price=0
while True:
    product=str(input("Enter the product Name :"))
    price=int(input("Enter the Price :"))
    print("Your product is ",product)
    print("Your product price :",price)
    Total_price +=price
    choice=str(input("IF YOU WANT TO ADD ANOTHER PRODUCT TYPE (YES) ELSE TYPE (NO) :"))
    if choice.upper()=="YES":
        continue
    else:
        print("thankyou for visiting",Customer)
        print("Total amount to be paid :",Total_price)
        break
    
    
    
    
# Bank Account Management System
# Ek program banao jisme initial balance ₹5000 ho. User ko menu dikhaya jaye:
# Deposit Money
# Withdraw Money
# Check Balance
# Exit

Initial_balance=50000
total_balance=0
while True:
    user_choice=str(input("IF USER WANT TO DEPOSIT TYPE (D) , WITHDRAW (W), CHECK BALANCE (C) :"))
    if user_choice.upper()=="D":
        print("enter the deposit amount")
        Deposit=int(input("enter the amount"))
        Initial_balance=Initial_balance+Deposit
        print("Your total Amount =",Initial_balance)
    elif user_choice.upper()=="W":
        print("enter the amount to be withdraw :")
        withdraw=int(input("Enter the amount to be withdraw :"))
        Initial_balance=Initial_balance-withdraw
        print("your total amount :",Initial_balance)
    elif user_choice.upper()=="C":
        print("your total balance :",Initial_balance)
    else:
        print("thankyou")
    continue_transaction=str(input("IF USER WANT TO CONTINUE TYPE (YES) ELSE (NO)"))
    if continue_transaction.upper()=="YES":
        continue
    else:
        print("thank you for transaction")
        break
        
        