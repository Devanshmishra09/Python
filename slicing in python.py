#slicing in python 
a="Hello, World!"
print(a[0:5])    #returns 'Hello'
print(a[7:12])   #returns 'World'
print(a[-6:-1])  #returns 'World'
print(a[-6:])    #returns 'World!'
print(a[:5])     #returns 'Hello'
print(a[::2])    #returns 'Hlo ol!'
print(a[1:5:2])  #returns 'el'

# reverse the string
print(a[::-1])   #returns '!dlroW ,olleH'
print(a[::])     #returns 'Hello, World!'


#type casting in python
a=10
print(type(a)) #returns <class 'int'>


a=10.5
print(type(a)) #returns <class 'float'> 

a="Hello"
print(type(a)) #returns <class 'str'>

