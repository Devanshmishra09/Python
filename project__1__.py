# import os

# FILE_NAME = "students.txt"

# def add_student():
#     print("\n--- Add New Student Record ---")
#     # 1. Take inputs: Name, Roll Number, and 3 Marks
#     # 2. Use Operators to calculate Total, Percentage, and Grade (if-else)
#     # 3. Open file in append mode: open(FILE_NAME, "a")
#     # 4. Write data as a comma-separated line and close file
#     pass

# def view_students():
#     print("\n--- All Student Records ---")
#     # 1. Check if file exists using os.path.exists(FILE_NAME)
#     # 2. Open file in read mode: open(FILE_NAME, "r")
#     # 3. Use a loop to read line by line, split by comma, and print cleanly
#     pass

# def search_student():
#     print("\n--- Search Student ---")
#     # 1. Take Roll Number input from user
#     # 2. Open file in read mode and loop through lines
#     # 3. If roll number matches, print details and set a flag
#     # 4. If loop ends and flag is false, print "Not Found"
#     pass

# def analyze_results():
#     print("\n--- Result Analysis & Statistics ---")
#     # 1. Open file in read mode
#     # 2. Track total students, running total of marks for average, pass/fail counts
#     # 3. Use loops and conditionals to find highest/lowest scores
#     # 4. Print the final summary statistics
#     pass

# def main():
#     while True:
#         print("\n==============================")
#         print(" STUDENT MANAGEMENT SYSTEM ")
#         print("==============================")
#         print("1. Add New Student")
#         print("2. View All Students")
#         print("3. Search Student")
#         print("4. Result Analysis")
#         print("5. Exit")
        
#         choice = input("Enter your choice (1-5): ")
        
#         if choice == '1':
#             add_student()
#         elif choice == '2':
#             view_students()
#         elif choice == '3':
#             search_student()
#         elif choice == '4':
#             analyze_results()
#         elif choice == '5':
#             print("Thank you for using the system. Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please enter a number between 1 and 5.")

# # Run the program
# if __name__ == "__main__":
#     main()


import os

with open("Students_Record","w") as f:
    f.write("__________Students record_________\n")
    f.close()
    
    
def add_students():
    Name= str(input("Enter the students name :"))
    Roll_no= int(input("Enter the students Roll_No :"))
    Python=int(input("Enter the Python subject marks :"))
    MySQL=int(input("Enter the MYSQL subject marks :"))
    PowerBI=int(input("Enter the PowerBI subject marks :"))
    Tebular=int(input("Enter the Tebular subject marks :"))
    Excel=int(input("Enter the Excel subject marks :"))
    Average=(Python+MySQL+PowerBI+Tebular+Excel)/5
    print(Average)
    Percentage=(((Python+MySQL+PowerBI+Tebular+Excel)/500)*100)
    print(Percentage,("%"))
    if Percentage>=90:
        print("A Grade")
    elif Percentage>=85:
        print("B Grade")
    elif Percentage>=65:
        print("C Grade")
    elif Percentage>=45:
        print("D Grade")
    elif Percentage>=33:
        print("E Grade")
    else:
        print("___FAIL___")

        
    with open("Students_Record","a")as f:
        f.write(f"Student name :{Name}\n")
        f.write(f"Students roll no :{Roll_no}\n")
        f.write(f"Python Marks:{Python}\n")
        f.write(f"MYSQL Marks : {MySQL}\n")
        f.write(f"PowerBI Marks : {PowerBI}\n")
        f.write(f"Tebular Marks :{Tebular}\n")
        f.write(f"Excel Marks :{Excel}\n")
        f.write(f"Average :{Average}\n")
        f.write(f"Percentage : {Percentage}\n")
        
        if Percentage>=90:
            f.write(("A Grade"))
        elif Percentage>=85:
            f.write("B Grade")
        elif Percentage>=65:
            f.write("C Grade")
        elif Percentage>=45:
            f.write("D Grade")
        elif Percentage>=33:
            f.write("E Grade")
        else:
            f.write("___FAIL___")
add_students()

def View_Students():
       print("\n--- All Student Records ---")
       os.path.exists("Students_Record")
       with open("Students_Record","r")as f:
            for line in f:

             words = line.strip().split(",")
             for item in words:
                print(item)
View_Students()


             
                
    
        