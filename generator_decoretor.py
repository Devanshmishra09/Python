# Generator : It is a special function which gives value line by line .
# It use Yield keyword :

# ex 
def generator():
    yield 1
    yield 2
    yield "hello world "
x=generator()
print(next(x))
print(next(x))

# Decoratore : in decorator we can decleare a function into a function and this type
# of function is called inner function :

# we can use @ this as a decorator 

# ex 
def outer():
    def inner():
        print(" this is a inner function ")
    inner()
    print(" this is yopur outter function ")
outer()

#  ex 2 

def a(x):
    def b():
        print("before changing ")
        x()
        print(" after changing ")
    return  b
@a
def c():
    print(" this is changed vlue of x ")
c()