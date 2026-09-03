# 7. Payment System — Abstraction + Polymorphism

# Create an abstract class Payment with an abstract method:

# pay(amount)

# Create:
# - CreditCardPayment
# - UPIPayment
# - CashPayment

# Requirements:
# - Each class should implement pay() differently.
# - Create one common function that accepts any Payment object.
# - Use polymorphism to process all payment types

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card.")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI.")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} in Cash.")

    
    def process_payment(payment, amount):
        payment.pay(amount)
        print("Payment System")
object=CreditCardPayment()
object.pay(1000)
object=UPIPayment()
object.pay(500)
object=CashPayment()
object.pay(200)


# # 
# 8. Library Management System — Classes + Encapsulation

# Create:
# - Book class
# - Member class
# - Library class

# Requirements:
# - A book should have title, author, and availability status.
# - A member should be able to borrow a book.
# - A member should be able to return a book.
# - Book availability should be encapsulated.
# - A book cannot be borrowed if it is already borrowed.

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_available = True  # Encapsulated attribute

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"{self.__title} has been borrowed.")
        else:
            print(f"{self.__title} is currently not available.")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"{self.__title} has been returned.")
        else:
            print(f"{self.__title} was not borrowed.")

    def is_available(self):
        return self.__is_available
object=Book("The Great Gatsby", "F. Scott Fitzgerald")
object.borrow()  
object.return_book() 

