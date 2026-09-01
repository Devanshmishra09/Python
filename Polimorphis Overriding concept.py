# polimorphism is the ability of an object to take on many forms. It allows methods to do different things based on the object it 
# is acting upon. In Python, polymorphism can be achieved through method overriding and operator overloading.


# Create a Vehicle class with a start() method. Create a Car class that overrides start() and prints "Car starts with key"

class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
obj=Car()
obj.start()

# Create a Bank class with an interest_rate() method. Create an SBI class that overrides it and returns SBI's interest rate.

class bank:
    def bank_intrest(self):
        print("bank intrest rate is 50")
class sbi(bank):
    def bank_intrest(self):
        print("sbi bank intrest rate is 70")
obj=sbi()
obj.bank_intrest()

# Create a Shape class with an area() method. Create a Circle class that overrides area() and calculates the area of a circle.

class shape:
    def area(self):
        print("area of shape")
class circle(shape):
    def area(self,radius):
        area=3.14*radius*radius
        print("area of circle is",area)
obj=circle()
obj.area(5)

# Create a Person class with a greet() method. Create a Student class that overrides greet() and prints "Hello, I am a student."

class person:
    def greet(self):
        print("Hello, I am a person")
class student(person):
    def greet(self):
        print("Hello, I am a student")
obj=student()
obj.greet()

