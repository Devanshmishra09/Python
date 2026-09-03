# 5. Student Result System — Encapsulation

# Create a Student class with:
# - name
# - roll_number
# - marks

# Requirements:
# - Marks should be private.
# - Create getter and setter methods for marks.
# - Marks must be between 0 and 100.
# - Calculate total marks.
# - Calculate percentage.
# - Display the student's complete result


class Student:
    def __init__(self,name,roll_no,marks1,marks2,marks3):
        self.name=name
        self.roll_no=roll_no
        self.__marks1=marks1
        self.__marks2=marks2
        self.__marks3=marks3
    def setter(self):
        total_marks=self.__marks1+self.__marks2+self.__marks3
        print(total_marks)
        if total_marks>=0 and total_marks<=300:
            print(total_marks)
        else:
            print("invalid marks")
    def getter(self):
        total_marks=self.__marks1+self.__marks2+self.__marks3
        percentage=total_marks/3
        print(percentage)
        print(self.name,self.roll_no,total_marks,percentage)

obj=Student("shubh",101,55,90,190)
obj.setter()
obj.getter()


# 6. E-Commerce Product System — Inheritance + Polymorphism

# Create a Product class with:
# - name
# - price
# - stock

# Create child classes:
# - Electronics
# - Clothing
# - Grocery

# Requirements:
# - Create a get_discount() method.
# - Override it in every child class.
# - Each product type should have a different discount.
# - Calculate the final price after discount.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
class Electronics(Product):
    def Get_disscount(self):
        discount=self.price-(self.price*12/100)
        print("Electronics Discount",discount)
        total=self.price-discount

        print(self.name)
        print(self.stock)
        print(self.price)
        print(total)
class clothing(Product):
    def Get_disscount(self):
        discount=self.price-(self.price*15/100)
        print("clothing Discount",discount)
        total=self.price-discount

        print(self.name)
        print(self.stock)
        print(self.price)
        print(total)
class grocery(Product):
    def Get_disscount(self):
        discount=self.price-(self.price*18/100)
        print("grocery Discount",discount)
        total=self.price-discount

        print(self.name)
        print(self.stock)
        print(self.price)
        print(total)
()
obj=Electronics("shubh",10000,2)
obj.Get_disscount()
ob=clothing("Devansh",1000,5)
ob.Get_disscount()
O=grocery("shivam",200000,1)
O.Get_disscount()
