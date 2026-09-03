# 1. Bank Account System — Encapsulation

# Create a BankAccount class with:
# - account_number
# - account_holder
# - balance

# Requirements:
# - Balance should not be directly accessible from outside the class.
# - Create deposit(amount) and withdraw(amount) methods.
# - Do not allow withdrawal if the balance is insufficient.
# - Create a get_balance() method to check the current balance.


class BankAccount:
    def __init__(self,Account_number,Account_holder,bacalce):
        self.__Account_number=Account_number
        self.__Account_holder=Account_holder
        self.__balance=bacalce
    def Deposit_amount(self):
        deposit=int(input("Enter the Deposit Amount :"))
        self.__balance+=deposit
        print(self.__balance)
    def Widthrawl(self):
        width=int(input("Enter the Widthrawl amount"))
        self.__balance-=width
        if width<=self.__balance:
                    print(" Your widthrawl amount",self.__balance)
        else:
            print("Invalid balance")
    def get_balance(self):
        print(" Your Balance ",self.__balance)
obj=BankAccount(123456789,"devansh",10000)
obj.Deposit_amount()
obj.Widthrawl()
obj.get_balance()


# 2. Employee Salary System — Inheritance + Polymorphism

# Create a base Employee class and three child classes:
# - Developer
# - Manager
# - Designer

# Requirements:
# - Each employee should have a name and base salary.
# - Create a calculate_salary() method.
# - Override calculate_salary() in each child class.
# - Each employee type should calculate the final salary differently.

class Employee:
    def __init__(self,name,salary):
         self.salary=salary
class Develover(Employee):
    def Calculate_salary(self,bonus):
        self.salary+=bonus
        print("Total Salary :",self.salary)
class Manager(Employee):
    def Calculate_salary(self,bonus):
        self.salary+=bonus
        print("Total Salary :",self.salary)
class Disiner(Employee):
    def Calculate_salary(self,bonus):
        self.salary+=bonus
        print("Total Salary :",self.salary)
obj=Develover("Shubh",15000)
obj.Calculate_salary(4000)
ob=Manager("Devansh",34000)
ob.Calculate_salary(10000)
O=Disiner("Shivam",12000)
O.Calculate_salary(2000)