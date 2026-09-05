# Encapsulation  is one of the fundamental concepts in object-oriented programming (OOP).
# It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit
# , typically a class. Encapsulation helps to protect the internal state of an object from unintended 
# interference and misuse by restricting access to its internal representation
#

# Types of Encapsulation in Python:
# 1. Public Encapsulation: In public encapsulation, the attributes and methods of a class are accessible from
# outside the class. This means that they can be accessed and modified directly by other parts of the program. 
# In Python, all attributes and methods are public by default.
#
# 
# 2. Protected Encapsulation: In protected encapsulation, the attributes and methods of a class are intended 
# to be accessed only within the class and its subclasses. In Python, this is indicated by a
# single underscore prefix (e.g., _attribute). While it is still possible to access these attributes 
# from outside the class, it is generally discouraged.
# 
# 
# 3. Private Encapsulation: In private encapsulation, the attributes and methods of 
# a class are intended to be accessed only within the class itself. In Python, this is 
# indicated by a double underscore prefix (e.g., __attribute). This provides a higher level of data 
# hiding and is more restrictive than protected encapsulation.

# questions:
# 1. Create a class called BankAccount with the following attributes:   
#    - account_number (private)
#    - account_holder (protected)
#    - balance (private)

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

object = BankAccount("123456789", "Alice Smith", 1000)
print(object.get_account_number())  # Accessing private attribute through getter
print(object.get_account_holder())  # Accessing protected attribute through getter
print(object.get_balance())         # Accessing private attribute through getter
print(object._account_holder)  # Accessing protected attribute directly (not recommended)


# 2. Create a class called Employee with the following attributes:
#    - name (public)
#    - salary (private)

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
        else:
            print("Salary cannot be negative.")
            
object = Employee("John Doe", 50000)
print(object.name)  # Accessing public attribute    
print(object.get_salary())  # Accessing private attribute through getter    


# Q3. Create a class called Student with the following attributes:
#    - name (public)
#    - age (protected)
#   - grade (private)
#   - Create getter and setter methods for each attribute.
#   - Create a method called display_info() that prints the student's information.

class Student:
    def __init__(self, name, age, grade):
        self.name = name          # Public attribute
        self._age = age           # Protected attribute
        self.__grade = grade      # Private attribute

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

    # Getter for grade
    def get_grade(self):
        return self.__grade

    # Setter for grade
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100.")

    # Method to display student information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Grade: {self.__grade}")
object = Student("Alice", 20, 90)
object.display_info()
object.set_age(21)
object.set_grade(95)
object.display_info()

