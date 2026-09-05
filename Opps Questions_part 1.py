# Opps questions with use of encapsulation, inheritance, polymorphism and abstraction all in one file

# Questions:
# 1. Create a class called BankAccount with the following attributes:   
#    - account_number (private)
#    - account_holder (protected)
#    - balance (private)
#  Implement methods to deposit, withdraw, and check balance. 
# Ensure that the balance cannot go negative.
# use encapsulation to protect the attributes.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number  # Private attribute
        self._account_holder = account_holder    # Protected attribute
        self.__balance = balance                  # Private attribute

    # Getter for account_number
    def get_account_number(self):
        return self.__account_number

    # Setter for account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Getter for account_holder
    def get_account_holder(self):
        return self._account_holder

    # Setter for account_holder
    def set_account_holder(self, account_holder):
        self._account_holder = account_holder

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            

object = BankAccount("123456789", "Alice Smith", 1000)
print(object.get_account_number())  # Accessing private attribute through getter
print(object.get_account_holder())  # Accessing protected attribute through getter
print(object.get_balance())         # Accessing private attribute through getter
object.deposit(500)                 # Depositing money
object.withdraw(200)                # Withdrawing money
print(object.get_balance())         # Accessing private attribute through getter
object.withdraw(2000)               # Attempting to withdraw more than balance



# Questions:
# 2. Create a class called Employee with the following attributes:
#    - name (public)
#    - salary (private)
#    Implement methods to get and set the salary. Use encapsulation to protect the salary attribute.


class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public attribute
        self.__salary = salary    # Private attribute

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print(f"Salary updated to {self.__salary}.")
        else:
            print("Salary cannot be negative.")

obj = Employee("John Doe", 50000)
print(obj.name)  # Accessing public attribute
obj.set_salary(60000)  # Updating salary
print(obj.get_salary())  # Accessing private attribute through getter
obj.set_salary(-1000)  # Attempting to set a negative salary