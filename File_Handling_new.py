#write a python program to create a .text file named "student.txt" and write the names of five student into it
with open("hello.txt","w")as f:
    f.write("shubh \n")
    f.write("Aryan\n")
    f.write("shivam\n")
    f.write("devansh\n")
    f.write("suraj\n")


#write  a python program to read and display the entire contents of a text file
with open("hello.txt","r")as f:
    print(f.read)

#question3
#write a python program to read and display the file line by line using a loop
with open("hello.txt","r")as f:
    for i in range(0,4):
        data=f.readline()
#question4
#write a python program to append the text "python is fun!" to an existing text file and then display the updated contents.
with open("hello.txt","a")as f:
    data=f.write("python is fun")
    print(data)


#question5
#write a python program to count the total number of lines in a text file.
with open("hello.txt","r")as f:
  data=f.readlines()
  print(len(data))

#question6
#write a python program to count the total number of words in a text file 

with open("hello.txt","r")as f:
    data=f.read()
    print(len(data))


#question7
#write a python program to count the total number of characters in a text
with open("hello.txt","r")as f:
    data=f.readline()
    print(len(data))


#question9
#write a python program to search for a given word in a text file and display whether  it is found or not.
with open("hello.txt","r")as f:
    data=f.read()
    d=str(input("enter a ch"))
    if d in data:
        print("found")
    else:
        print("not found")

