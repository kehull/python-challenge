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

# Use encoding for Windows

with open(employee_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add Employee ID
        Emp_ID.append(row[0])

        # Split name and add to First Name and Last Name
        str(row[1]).split(' ')
        First_Name.append(row[1])
        Last_Name.append(row[2])

        # Add DOB
        DOB.append(row[3])

        # Add SSN
        SSN.append(row[4])


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
    print(writer)