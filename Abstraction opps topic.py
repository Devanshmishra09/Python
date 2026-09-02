# Abstraction in Python is a process of hiding the implementation details and showing only the functionality to the user. 
# It helps in reducing programming complexity and effort. In Python, abstraction can be achieved using abstract classes and methods.



from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow! Meow!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.make_sound())
print(cat.make_sound())

# using abstraction in a different context, like shapes and their areas


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    @abstractmethod
    def A(self):
        pass
class Rectangle(Circle):
    @abstractmethod
    def a(self):
        pass
class Square(Rectangle):
    @abstractmethod
    def S(self):
        pass
class R(Square):
    def are(self):
        length = float(input("Enter the length of the square: "))
        area = length * length
        print(f"The area of the square is: {area}")
    def area(self):
        radius = float(input("Enter the radius of the circle: "))
        ar = 3.14 * radius * radius
        print(f"The area of the circle is: {ar}")
    def a(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area}")
    def S(self):
        side = float(input("Enter the side length of the square: "))
        area = side * side
        print(f"The area of the square is: {area}")
    def A(self):
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print(f"The area of the circle is: {area}")
        
obj=R()
obj.area()
obj.a()
obj.S()
obj.are()
