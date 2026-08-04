# example of writing to a file or opning a file in write modeor reading mode 
from socket import close

#

a=open("new file.py","w")
print(a.write("hello good morning"))
a.close()

#

a=open("new file.py","r")
print(a.read())
a.close()

#

a=open("new file.py","a")
print(a.write("hello good morning"))
a.close()

#

# reading a file line by line
a=open("new file.py","r")
print(a.readline())
a.close()

#

# read all lines of a file
a=open("new file.py","r")
print(a.readlines())
a.close()

#

# writelines to a file
a=open("new file.py","w")
lines=["hello good morning\n","how are you \n","have a good day \n"]
a.writelines(lines)
a.close()

#

# using of with statement to open a file or read a file or write a file
with open("new file.py","r") as a:
    print(a.read())

#

with open("new file.py","w") as a:
    a.write("hello good morning\n")
    a.write("how are you \n")
    a.write("have a good day \n")
    print("file written successfully")

#

# use with for zero division error
try:
    with open("new file.py","r") as a:
        print(a.read())
except ZeroDivisionError:
    print("division by zero is not possible")       

    
# printing or give  range of lines from a file to read a file or end with a specific line
with open("new file.py","r") as a:
    for line in a:
        if "how are you" in line:
            break
        print(line.strip())
        
        
# #

with open("new file.py", "r") as my_file:
    for i in range(1, 6):
        line = my_file.readline()
        if i >= 2:
            print(line, end="")

#

with  open("c.py","w")as c:
    c.write("hello good morning\n")
    c.write("how are you \n")
    c.write("have a good day \n")
    c.write("i am good \n")
    c.write("good work\n")
    c.write("file written successfully\n")
    
    
#


with open("c.py","r")as c:
    for i in range(1,7):
     line=c.readline()
     if i >= 2:
         print(line,end="")