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