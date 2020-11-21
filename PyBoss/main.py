import os
import csv

employee_data = os.path.join("Resources", "employee_data.csv")

# Lists to store data
Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

# open the file
with open(employee_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        # Add Employee ID to list
        Emp_ID.append(row[0])
        # Split name and add to First Name and Last Name lists
        Full_Name = str(row[1]).split(' ')
        First_Name.append(Full_Name[0])
        Last_Name.append(Full_Name[1])
        # Format birthdate adn add to DOB
        Split_DOB = str(row[2]).split('-')
        DOB.append(f'{Split_DOB[1]}/{Split_DOB[2]}/{Split_DOB[0]}')
        # Obscure first five digits of string and add to SSN
        Split_SSN =str(row[3]).split('-')
        SSN.append(f'***-**-{Split_SSN[2]}') 
        # Add State
        State.append(row[4]) #still working on this


# Zip lists together
cleaned_csv = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State)
# Set variable for output file
output_file = os.path.join("cleaned_data","pyboss_complete.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    # Write in zipped rows
    writer.writerows(cleaned_csv)
