# 3. Create a Bank Management System.
#    Implement SavingsAccount and CurrentAccount using inheritance.
#    Support deposit, withdrawal, interest calculation, and transaction history

class Bankaccount:
    def __init__(self,account_number,account_holder,balance,transaction_history=None):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = transaction_history if transaction_history is not None else  []
class SavingsAccount(Bankaccount):
    def __init__(self, account_number, account_holder, balance, interest_rate, transaction_history=None):
        super().__init__(account_number, account_holder, balance, transaction_history)
        self.interest_rate = interest_rate
        print(f"Savings Account created for {self.account_holder} with account number {self.account_number}.")
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print(f"Initial Balance: ${self.balance}")
        print(f"Transaction History: {self.transaction_history}")
        
class CurrentAccount(Bankaccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit, transaction_history=None):
        super().__init__(account_number, account_holder, balance, transaction_history)
        self.overdraft_limit = overdraft_limit
        print(f"Current Account created for {self.account_holder} with account number {self.account_number}.")
        print(f"Overdraft Limit: ${self.overdraft_limit}")
        print(f"Initial Balance: ${self.balance}")
        print(f"Transaction History: {self.transaction_history}")

object1 = SavingsAccount("SA123", "Alice", 1000, 0.05)
object2 = CurrentAccount("CA456", "Bob", 500, 200)
object1.transaction_history.append("Deposited $100")
object1.transaction_history.append("Withdrew $50")
object2.transaction_history.append("Deposited $200")
object2.transaction_history.append("Withdrew $100")


# 4. Design an Online Shopping Cart.
#    Create Product, Cart, Customer, and Order classes.
#    Implement add/remove products, quantity management, discount, tax, and final bill calculation.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} (Quantity: {self.quantity})"
    def update_quantity(self, quantity):
        self.quantity += quantity
        print(f"Updated quantity of {self.name}: {self.quantity}")
class Cart:
    def __init__(self):
        self.items = []
        print("Shopping cart created.")
    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append((product, quantity))
            product.update_quantity(-quantity)
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Insufficient stock for {product.name}. Available: {product.quantity}")
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
        print(f"Customer created: {self.name}")
    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)
        
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.total_amount = 0
        print(f"Order created for {self.customer.name}.")
    def calculate_total(self, discount=0, tax=0):
        for product, quantity in self.customer.cart.items:
            self.total_amount += product.price * quantity
        self.total_amount -= self.total_amount * discount
        self.total_amount += self.total_amount * tax
        print(f"Total amount after discount and tax: ${self.total_amount:.2f}")
class ShoppingCartSystem:
    def __init__(self):
        self.products = []
        self.customers = []
        print("Shopping Cart System initialized.")
    def add_product(self, product):
        self.products.append(product)
        print(f"Product added: {product}")
    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer added: {customer.name}")
object1 = Product("Laptop", 1000, 10)
object2 = Product("Smartphone", 500, 20)
object3 = Product("Headphones", 100, 30)
customer1 = Customer("Alice")
customer1.add_to_cart(object1, 1)
customer1.add_to_cart(object2, 2)
customer1.add_to_cart(object3, 3)
customer2 = Customer("Bob")
customer2.add_to_cart(object1, 2)
customer2.add_to_cart(object2, 1)
order1 = Order(customer1)   
object = ShoppingCartSystem()
object.add_product(object1)
object.add_product(object2)
object.add_product(object3)
object.add_customer(customer1)
object.add_customer(customer2)