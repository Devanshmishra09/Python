# Encapsulation in Python is a process of wrapping data and methods together in a single unit (class). 
# It helps in hiding the internal details of an object and exposing only the necessary information to the outside world. 
# This is achieved by making the attributes and methods of a class private and providing public methods to access and modify them.

# its main purpose is to protect the internal state of an object from unintended interference and misuse.
# in Python, encapsulation is implemented using access modifiers, which determine the visibility of class members
# (attributes and methods).

# Simple example of encapsulation in Python:

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance
    

account = BankAccount("123456789", 1000)
account.deposit(500)  # Deposited: 500. New balance: 1500   
account.withdraw(200)  # Withdrew: 200. New balance: 1300
print(f"Current balance: {account.get_balance()}")


# Overriding the __str__ method to provide a string representation of the object
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def __str__(self):
        return f"Person(Name: {self.__name}, Age: {self.__age})"
obj=Person("John", 30)
print(obj) 


