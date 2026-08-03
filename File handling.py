#  File handling
# Read, Write, Append, and Delete files in Python
# read mode - 'r'
# write mode - 'w'
# append mode - 'a'
# delete mode - 'x'

# Q 1 Write a Python program to create a new file and write some text into it.
with open("newfile.txt", "w") as f:
    f.write("Hello, this is a new file.\n")
    f.write("This file is created using Python.\n")
    f.write("We can write multiple lines into the file.\n")
print("File created and text written successfully.")

# Q 2 Write a Python program to read the contents of a file and print it to the console.
with open("newfile.txt", "r") as f:
    content = f.read()
    print("Contents of the file:")
    print(content)
    
# Q 3 Write a Python program to append some text to an existing file.
with open("newfile.txt", "a") as f:
    f.write("This line is appended to the file.\n") 
    print("Text appended successfully.")
    
# Read Mode 
with open("newfile.txt", "r") as f:
    content = f.read()
    print("Contents of the file after appending:")
    print(content)
    
# write Mode
with open("newfile.txt", "w") as f:
    f.write("This is a new content of the file.\n")
    print("File overwritten successfully.")
    
# append Mode
with open("newfile.txt", "a") as f:
    f.write("This line is appended to the file again.\n")
    print("Text appended successfully.")

# delete Mode
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted successfully.")
    

# append Mode
with open("newfile.txt", "a") as f:
    f.write("This line is appended to the file again.\n")
    print("Text appended successfully.")
    

