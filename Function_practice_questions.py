# Create a function to calculate the average marks of students.
def marks(number):
    total=0
    for num in number:
        total=total+num
    average=total/len(number)
    return average
number=(76,88,66,78)
print(marks(number))

# Create a function to find the highest sales value from a sales list.
def sales(number):
    highest=number[0]
    for num in number:
        if num>0:
            highest=num
    return highest
number=(566,888,655,876,8898)
print(sales(number))

# # Create a function to count how many sales are above ₹10,000.
def sales(number):
    count=0
    for num in number:
        if num>10000:
            count=count+1
    return count
number=(12000,45000,645,678,5586,8767,4565,1000000,1234567)
print(sales(number))

# # Create a function to calculate total sales from a list.
def total_sales(number):
    total=0
    for num in number:
        total=total+num
    return total
number=(1200,700,355,7666)
print(total_sales(number))


# # Create a function to find the average salary from a list.

def average_salary(number):
    total=0
    for num in number:
        total=total+num
    average=total/len(number)
    return average
number=(40000,50000,60000)
print(average_salary(number))

# Create a function to count employees whose salary is greater than ₹50,000.
def count_employees_salary(number):
    count=0
    for num in number:
        if num>50000:
            count=count+1
    return count
number=(678988,2334,344,569797,23334,77888)
print(count_employees_salary(number))

# Create a function to remove negative values from a dataset.

def result(number):
    result=[]
    for num in number:
        if num>0:
            result.append(num)
    return result
number=(34,-54,56,-65,55,66,-66)
print(result(number))

# Create a function to find the second-largest value in a list.
def second_largest(number):
    largest=number[0]
    second=number[0]
    for num in number:
        if num>largest:
            second=largest
            largest=num
        elif num<second and num!=second:
            second=num
    return second
number=(55,656,67,465,6676,567)
print(second_largest(number))



# Create a function to calculate the percentage of positive values in a dataset.

def positive_value(number):
    positive=0
    for num in number:
        if num>0:
            positive=positive+1
        percentage=positive/len(number)*100
    return percentage
number=(34,54,55,-55,-55,56,-65)
print(positive_value(number))


# Create a function that accepts a list of numbers and returns total, average, maximum, and minimum.

def all(number):
    largest=number[0]
    smallest=number[0]
    total=0
    for num in number:
        total=total+num
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
   
    average=total/len(number)
    return average,total,largest,smallest
number=(56,97,76,77,86,56,56)
print(all(number))