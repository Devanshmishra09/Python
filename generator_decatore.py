# generator question
def calculate(number):
    sum=0
    for num in number:
        sum=sum+num
    yield sum
number=(56,78,99,60,89)
x=(calculate(number))
print(next(x))



# generator question
def genrator():
    yield 1
    yield 2
x=genrator()
print(next(x))
print(next(x))

# simple fuction question
def add():
    a=20
    b=30
    print(a+b)
add()




# decorator question
def outer():
    def inner():
        print("this is innner function")
    inner()
    print("this is outer function ")
outer()




#decorator question
def decorator(fun):
    def wrapper():
        print("before function")
        fun()
        print("after function")
        
    return wrapper
@decorator
def hello():
    print("hello bhai how are you")
hello()

