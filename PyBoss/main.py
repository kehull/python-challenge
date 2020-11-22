import os
import csv
from us_state_abbrev import us_state_abbrev

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
        # Format birthdate and add to DOB list
        Split_DOB = str(row[2]).split('-')
        DOB.append(f'{Split_DOB[1]}/{Split_DOB[2]}/{Split_DOB[0]}')
        # Obscure first five digits of SSN and add to SSN list
        Split_SSN =str(row[3]).split('-')
        SSN.append(f'***-**-{Split_SSN[2]}') 
        # Read external dictionary of state abbreviations into the code, then search within the keys of that dictionary for the state's full name and return the value, which is the state's abbreviation.
        State_Name=str(row[4])
        for long_name, abbrev in us_state_abbrev.items():
            if State_Name in us_state_abbrev:
                State_Name=abbrev
                State.append(abbrev)

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
