# file handling with binary mode :
# write mode:
with open("New file.txt","wb")as f:
    f.write(b"Hey how are you\n")
    f.write(b"I am Data Anaylatics student")
    
# with simple mode :
f=open("new file.txt","wb")
d=f.write(b"Hey how are you")
print(d)
f.close()

# Append Mode :
with open("New file.txt","ab")as f:
    f.write(b"hey how are you")
    

# Simple mode :
f=open("New file.txt","ab")
d=f.write(b"I am fine")
print(d)
f.close()

# read mode :
with open("New file.txt","rb")as f:
    print(f.read())
    

# simple mode:
f=open("New file.txt","rb")
print(f.read())
f.close()