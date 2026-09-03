# 3. ehicle Rental System — Inheritance + Polymorphism

# Create a Vehicle class with:
# - brand
# - model
# - rental_price

# Create three child classes:
# - Car
# - Bike
# - Truck

# Requirements:
# - Create a calculate_rent(days) method.
# - Each vehicle type should calculate rent differently.
# - Use method overriding.

class Vehicle:
    def __init__(self,Brand,Model,rental_price):
        self.rental_price=rental_price
class Car(Vehicle):
    def Calculate_rent(self,Rent):
        self.rental_price+=Rent
        print(self.rental_price)
class Bike(Vehicle):
    def Calculate_rent(self,Rent):
        self.rental_price+=Rent
        print(self.rental_price)
class Truck(Vehicle):
    def Calculate_rent(self,Rent):
        self.rental_price+=Rent
        print(self.rental_price)
obj=Car("Tesla","xuv700",10000)
obj.Calculate_rent(2000)
ob=Bike("splendor","hero",1500)
ob.Calculate_rent(1000)
o=Truck("contener","Tata",30000)
o.Calculate_rent(5000)


# 4. Shape Area Calculator — Abstraction + Polymorphism

# Create an abstract class Shape with an abstract method area().

# Create:
# - Circle
# - Rectangle
# - Triangle

# Requirements:
# - Each class must implement area().
# - Create objects of all three classes.
# - Store them in a list.
# - Use a loop to calculate the area of every shape.

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
cases=[Circle(5),Rectangle(4,6),Triangle(3,8)]
for case in cases:
    print(f"Area of {case.__class__.__name__}: {case.area()}")
    
ob=Circle(5)
print("Area of Circle :",ob.area())
ob=Rectangle(4,6)
print("Area of Rectangle :",ob.area())
ob=Triangle(3,8)
print("Area of Triangle :",ob.area())
