from functools import*
lst=[52,4,69,36,487,68,38,6,866,86]
def a(x,y):
    return x if x>y else y
print(reduce(a,lst))