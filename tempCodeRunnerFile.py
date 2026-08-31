def add_students():
    Name= str(input("Enter the students name :"))
    Roll_no= int(input("Enter the students Roll_No :"))
    Python=int(input("Enter the Python subject marks :"))
    MySQL=int(input("Enter the MYSQL subject marks :"))
    PowerBI=int(input("Enter the PowerBI subject marks :"))
    Tebular=int(input("Enter the Tebular subject marks :"))
    Excel=int(input("Enter the Excel subject marks :"))
    
    Average=(sum(Python,MySQL,PowerBI,Tebular,Excel))/5
    Percentage=((sum(Python,MySQL,PowerBI,Tebular,Excel))/500)*100