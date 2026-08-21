#single inheritance
class student:
     def __init__(self,name,age):
         self.name=name
         self.age=age

     def display(self):
         print(self.name,self.age,"this is present class")

class teachers(student):
     pass
aa=student("Devansh",19)
aa.display()

# Multilevel
class student:
     def __init__(self,name):
         self.name=name
     def display(self):
         print(self.name,"this is first class")

class teacher(student):
     def __init__(self,name,age):
         self.age=age
         super().__init__(name)
     def show(self):
         print(self.age,"this is second class")

class principle(teacher):
    pass
aa=principle("Devansh",20)
aa.display()
aa.show()

# Hierarchical
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(self.name,self.age,self.marks,"this is first class")
class student1(student):
    pass
class student2(student1):
    pass

ab=student1("shubh",19,20)
aa=student2("divansh",20,70)
ab.display()
aa.display()

# mutiple

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age,"this  is first class")

class teacher:
    def show(self):
        print("this is second class")
    

class priciple(student,teacher):
    pass
aa=priciple("Devansh",20,)
aa.display()
aa.show()