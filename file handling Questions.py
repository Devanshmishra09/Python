# File Handling Questions
# Q 1 Write a Python program to create a new file and write some text into it.
with open("newfile.txt", "w") as f:
    f.write("Hello, this is a new file.\n")
    f.write("This file is created using Python.\n")
    f.write("We can write multiple lines into the file.\n")
    
# Q 2 Write a Python program to read the contents of a file and print it to the console.
with open("newfile.txt", "r") as f:
    content = f.read()
    print("Contents of the file:")
    print(content)

# Q 3 Write a Python program to append some text to an existing file.
with open("newfile.txt", "a") as f:
    f.write("This line is appended to the file.\n") 
    print("Text appended successfully.")

# Q 4 Write a Python program to read a file line by line and print each line to the console.
with open("newfile.txt", "r") as f:
    print("Reading file line by line:")
    for line in f:
        print(line.strip())
        
# Q 5 Write a Python program to delete a file.
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted successfully.")
    
# Q 6 Write a Python program to check if a file exists.

if os.path.exists("newfile.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# Q 7 Write a Python program to copy the contents of one file to another file.
import shutil
shutil.copy("newfile.txt", "copyfile.txt")
print("File copied successfully.")


# Q 8 Write a Python program to move a file from one location to another.
shutil.move("copyfile.txt", "new_location/copyfile.txt")
print("File moved successfully.")

# Q 9 Write a Python program to rename a file.
os.rename("newfile.txt", "renamedfile.txt")
print("File renamed successfully.")


# Q 10 Write a Python program to get the size of a file in bytes.

size = os.path.getsize("newfile.txt")
print(f"Size of the file: {size} bytes")

