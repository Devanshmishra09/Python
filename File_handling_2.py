#  question 1->Create a file named data.txt and write "python file handling"into it.
with open("hello.txt","w")as f:
    print(f.write("hello ji"))


#question 2->Read the data.txt file and print its  complete content.
with open("hello.txt","r")as f:
    print(f.read())



#question 3->Add "I am learning python" to data.txt without deleting the existing content.
with open("hello.txt","a")as f:
    print(f.write(" I am learning python"))

#question 4->Read a file and count the total number of lines present in it.
with open("hello.txt","r")as f:
    print(len(f.readlines()))

#question 5->Read a file and count the total number of words present in it.
with open("hello.txt","r")as f:
    a=f.read()
    words=a.split()
    print(len(words))

#question 6->Read a file and count the total number of characters,excluding spaces.
with open("hello.txt","r")as f:
    a=f.read()
    print(len(a))

#question 7->Take a word from the user and check whether that word exists in a file or not.
with open("hello.txt","r")as f:
    a=f.read()
if "python" in a:
    print("that word are present")
else:
    print("that word are not present")


#question 8->Read the contents of source.txt and copy them into destination1.txt
with open("hello.txt","r")as f:
    a=f.read()
with open("destination1.txt","w")as f:
    print(f.write(a))


