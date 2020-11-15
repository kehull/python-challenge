#import the os and document
import os
import csv
# Path to collect data from the Resources folder
bank_csv = os.path.join( 'Resources', 'budget_data.csv')

def summary(bank_info):
    date = str(bank_info[0])
    money = int(bank_info[1])


    Total_Months = sum(1 for row in csvreader) #count rows of document
    Total = "TBA" #total of money column
    Avg_Change = "TBA" #Total / Total_Months
    Greatest_Increase = "TBA" #this will be a formula!
    Greatest_Decrease = "TBA" #this will be a formula!

    #Set up code to process final results
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: {Total}")
    print(f"Average_Change: {Avg_Change}")
    print(f"Greatest Increase in Profits: {Greatest_Increase}")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease}")



#Add a line of code that will export a text file with the results


# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        summary(row)
   