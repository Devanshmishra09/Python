
with open("c.py","r")as c:
    for i in range(1,7):
     line=c.readline()
     if i >= 2:
         print(line,end="")