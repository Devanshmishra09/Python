
# Student Marks and Grade
# Write a function calculate_result(marks) that takes a list of marks and calculates:

# Total marks
# Percentage
# Grade
def calculate_result(marks):
    total=0
    for num in marks:
        total=total+num
    Percentage=total/5
   
    if Percentage>=90 and  Percentage<=100:
        print("A Grade")
    elif Percentage>=80 and Percentage<=90:
        print("B Grade")
    elif Percentage>=70 and Percentage<=80:
        print("c Grade")
    elif Percentage>=60 and Percentage<=70:
        print("d Grade")
    elif Percentage>=50 and Percentage<=60:
        print("E GRade")
    else:
        print("Fail")
    return Percentage,total
marks=(95,86,98,76,96)
print(calculate_result(marks))       

