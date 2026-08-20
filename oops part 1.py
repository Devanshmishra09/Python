# creating data types using oops:
class fraction:
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
      new_num=self.num*other.den + other.num*self.den
      new_den=self.den*other.den
      return '{}/{}'.format(new_num,new_den)

    def __sub__(self,other):
        new_num=self.num*other.den - self.den-other.num
        new_den=self.den-other.den
        return '{}/{}'.format(new_num,new_den)

    def __mul__(self,other):
         new_num=self.num*other.num
         new_den=self.den*other.den
         return '{}/{}'.format(new_num,new_den)

    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*self.num
        return '{}/{}'.format(new_num,new_den)
    
fr1=fraction(3,4)
fr2=fraction(1,2)
print(fr1)
print(fr2)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)