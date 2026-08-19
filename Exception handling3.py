#question9->. Calculator with Finally

#Create a calculator that performs addition, subtraction, multiplication, and division.

#Requirements:
#- Take two numbers from the user.
#- Take an operator (+, -, *, /).
#- Handle invalid numeric input using ValueError.
#- Handle division by zero using ZeroDivisionError.
#- Use finally to print "Calculator execution completed".


try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))

    operator=input("enter a (+,-,/,*)")

    if operator=="+":
     print(a+b)

    elif operator=="-":
       print(a-b)

    elif operator=="/":
       print(a/b)

    elif operator=="*":
       print(a*b)

    else:
       print("invalid operator")

except ValueError:
    print("invalid numeric input")

except ZeroDivisionError :
    print("cannot divide by zero")

finally:
    print("calculator excution completed")




#question10->. Student Registration System

#Create a simple student registration program.

#Take the following inputs:
#- Student name
#- Age
#- Marks

#Requirements:
#- Age and marks must be numeric.
#- Age must be between 18 and 60.
#- Marks must be between 0 and 100.
#- Use raise to generate appropriate

try:
    name=str(input("enter a name"))
    age=int(input("enter a age"))
    marks=int(input("enter a marks"))

    if age<18 or age>60:
        raise Exception("error,age must be between 18 and 60")
    if marks<0 or marks>100:
        raise Exception("error,marks must be between 0 and 100")
    print("student registration successfully")
    print(name,"name")
    print(age,"age")
    print(marks,"marks")

except ValueError:
    print("age and marks must be numeric")
except Exception as f:
    print(f)