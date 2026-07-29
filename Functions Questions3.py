# Q 1 First, use filter() to select all even numbers, then use map() to find their squares.

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Even=(list(filter(lambda x: x%2==0,lst)))
print(list(filter(lambda x: x%2==0,lst)))
Square=(list(map(lambda x:x*x,Even)))
print(Square)

# Q 2 First, use filter() to select all numbers greater than 50, then use reduce() to find their sum.

from functools import*
lst=[25,2525,8,48,278,281,825,72,82,7,2857,28,1,58,2,7,21,7,2,47,25,2]
greater=(list(filter(lambda x:x>50,lst)))
print(greater)
sum=(reduce(lambda x,y:x+y,greater))
print(sum)


# Q 3 Use filter() with a simple function to find all palindrome words in a list.

lst=[ "Mom", "dad", "wow", "pop","rewa", "eye", "gig", "nun", "kayak","dev"]
def find(x):
    return x==x[::-1]
print(list(filter(find,lst)))


# Q 4 Given a list of student marks, remove all marks below 40 using filter(),
# then add 5 bonus marks to the remaining marks using map().

lst=[90,40,50,60,78,34,95,73,29,87]
marks=(list(filter(lambda x:x>40,lst)))
print(marks)
bonus=(list(map(lambda x:x+5,marks)))
print(bonus)


# Q 5 Given a list of salaries, filter salaries greater than 50,000 and increase each salary by 10% using map().

lst=[20000,30000,70000,80000,90000,100000,75000]
Salary=list(filter(lambda x:x>50000,lst))
print(Salary)
increase=list(map(lambda x:x*1.10,Salary))
print(increase)

# Q 6 Given a list of student dictionaries, use filter() to find students whose age is 18 or above

lst= [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 18},
    {"name": "David", "age": 16}
]
adult=list(filter(lambda n:n["age"]>=18,lst))
print(adult)


# Q 7 Given a list of employee dictionaries, use map() to increase each employee's salary by 20%.

employee= [
    {"name": "Alice", "salary": 17000},
    {"name": "Bob", "salary": 19000},
    {"name": "Charlie", "salary": 18000},
    {"name": "David", "salary": 16000}
]
increase=list(map(lambda x:x["salary"]*1.2,employee))
print(increase)