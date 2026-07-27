# Data types
# 1 List : 

a=["abc","xyz","mno"]
print(a)
print(id(a))
a[0]="suraj"
print(a[0])
print(a)
print(type(a))


# 2 tupples:

a=("devansh","shivam","shubh")
print(type(a))
print(a)


# 3 set :

a={10,20,30,4,0,50}
print(type(a))

# empity sets
a=set()
print(type(a))

# inserting order 

a={1,2,3,6}
b={5,9,10,4,3}
a.update(b)
print(a)

# Remove :

a={1,5,4,6,8,6}
a.remove(5)
print(a)

# Pop :

a={10,20,30,40,50,60}
a.pop()
print(a)

# union:
a={1,2,3,6}
b={5,9,10,4}
print(a|b)

# Intersection :
a={1,2,3,6}
b={5,9,10,4,3,5,7,1,6,3,2,1}
print(a&b)

# clear
a={1,2,3,6}
print(a.clear)

# Difference :
a={1,2,3,4,5}
b={1,4,3,5,7,8,9,6,2}
print(a.difference(b))

# symmetric diffeence :
a={1,2,3,6}
b={5,9,10,4,3,5,7,1,6,3,2,1}
print(a.symmetric_difference(b))

# Dictonary :
a={
    "name":"xyz",
    "name2":"abc",
    "name3":"mno"
}
print(type(a))
print(a)

# clear dictonary:
a={
    "name":"xyz",
    "name2":"abc",
    "name3":"mno"
}
print(type(a))
print(a)
del (a)

# get :
a={
    101:"xyz",
    102:"abc",
    103:"mno"
    }
print(type(a))
print(a)
a.get(103)
print(a)

# pop :
a={
    101:"xyz",
    102:"abc",
    103:"mno"
    }
print(type(a))
print(a)
a.pop(103)
print(a)

# write a program to print only value in dictonary :


a={
    101:"xyz",
    102:"abc",
    103:"mno"
    }
for i in a:
    print(a[i])

# print with keywords:
a={
    101:"xyz",
    102:"abc",
    103:"mno"
    }
for i in a:
    print(i,":",a[i])
    

# Frozen set :
a=frozenset([10,20,30,4,0,50,78,52])
print(type(a))