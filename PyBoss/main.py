#import the os and document
import os
import csv
# Path to collect data from the Resources folder
election_csv = os.path.join('employee_data.csv')
output = []

with open(election_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_csv, delimiter=',')
    next(csvreader)

#def summary(csvreader):
for row in csvreader:
    output.append(row.split(' '))
    print(output)
