# Question 7

# Ek decorator banao jo function execute hone ke baad:

# Function Ended

# print kare.

# Expected output:

# Hello
# Function Ended

def a(x):
    def b():
        x()
        print("function end")
    return b
        
@a
def c():
    print("hello")
c()


# Ek decorator banao jo function ki return value ko double karke return kare.
def add(x):
    def b():
        return x()*2
    return b
@add
def c():
    return 10
print(c())


# Ab Question 9 karte hain: age 18+ hai to function chale, warna nahi.
def age_check(x):
    def b(age):
        if age>=18:
            return x(age)
        else:
            return "age 18+ nhi hai yaar"
    return b
@age_check
def c(age):
    return "welcome"
print(c(2))
