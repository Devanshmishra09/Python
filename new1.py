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
File_name="College.txt"

def add_student():
    print("===== Add New Student Record=====\n")
    Name=input("  Enter the Name of Student")
    Roll_no=int(input(" enter the roll no "))
    Python=int(input("enter the marks of python "))
    Tebaule=int(input("enter the marks of Tebaule "))
    Excel=int(input("enter the marks of Excel "))
    Sql=int(input("enter the marks of SQL  "))
    Powerbi=int(input("enter the marks of powerbi "))
    total=Python+Sql+Tebaule+Excel+Powerbi
    percentage=total/5
    if percentage>=90:
        print(" Grade A")
    elif percentage>=75:
        print(" Grade B")
    elif percentage>=45:
        print(" Grade C")
    else:
        print(" FAIL ")
    kj="==== Student Record  ====\n"   
    print(kj)
    with open(File_name,"a") as f:
        f.write(f"Name  :  {Name}\n")
        f.write(f"Roll_no  :  {Roll_no}\n")
        f.write(f"Python  :  {Python}\n")
        f.write(f"Tebaule  :  {Tebaule}\n")
        f.write(f"Sql  :  {Sql}\n")
        f.write(f"PowerBi  :  {Powerbi}\n")
        f.write(f"Total  :  {total}\n")
        f.write(f"Percentage  :  {percentage}\n")
        if percentage>=90:
            f.write(" Grade A\n")
        elif percentage>=75:
            f.write(" Grade B\n")
        elif percentage>=45:
            f.write(" Grade C\n")
        else:
            f.write(" FAIL \n")
        f.write(kj)
add_student()
def view_Student():
    print("====== Students Record ======")
    os.path.exists(File_name)
    with open(File_name,"r") as f:
        for line in f:
            word=line.strip().split(",")
            for j in word:
                print(j)
view_Student() 
def search_student():
    print("===== Your search record =====")
    roll=int(input("Enter the roll no "))
    found