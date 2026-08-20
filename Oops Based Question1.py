 # 1. Student Class
# Create a Student class with:
# - college_name as class variable
# - name and marks as instance variables
# - display() as instance method
# - change_college() as class method
# - check_marks() as static method

class student:
     college_name="lit college"
     def __init__(self,name):
       self.name=name

     def s(self):
          print(self.name,self.marks,student.college_name)
     @classmethod
     def cc(cls,nn):
         cls.college_name=nn
         print(cls.college_name)
     @staticmethod
     def marks(nn):
         if(nn>33):
             print("pass")
         else:
             print("failed")

# c=student("shivam sant",);
# student.cc("aktu ")
# student.marks(20)
# c.s();


#2. Employee Class
#Create an Employee class with:
#- company as class variable
#- name and salary as instance variables
#- display() as instance method
#- change_company() as class method
#- check_salary() as static method


class Empolyee():
    company_name="xyz"
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"name:{self.name},salary:{self.salary}")

    @classmethod
    def a(cls,ab):
        cls.company_name=ab
        print(cls.company_name)

    @staticmethod
    def check_salary(salary):
        return salary>0;
a=Empolyee("shivam",2000000)
a.display()
Empolyee.a("amazon")
print(Empolyee.check_salary(100000))


# 4. Product Class
# Create a Product class with:
# - store_name as class variable
# - name and price as instance variables
# - display() as instance method
# - change_store() as class method
# - check_price() as static method

class Product():
    store_name="vodka"
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display(self):
        print(f"name{self.name},price{self.price}")


    @classmethod
    def aa(cls,ss):
        cls.store_name=ss
        print(cls.store_name)

    @staticmethod
    def check_price(price):
        return price>0

a=Product("Fratelli J'Noon REd","4500")
a.display()
Product.aa("wine")
print(Product.check_price(4500))



# 5. Vehicle Class
# Create a Vehicle class with:
# - showroom as class variable
# - brand and price as instance variables
# - display() as instance method
# - change_showroom() as class method
# - check_price() as static method


class vehicle():
    showroom="Bike"
    def __init__ (self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        print(f"brand{self.brand},price{self.price}")

    @classmethod
    def aa(cls,ss):
        cls.showroom=ss
        print(cls.showroom)

    @staticmethod
    def check_price(price):
        return price>0
aa=vehicle("Fortuner","5800000")    
aa.display()
vehicle.aa("car")
print(vehicle.check_price(5800000))