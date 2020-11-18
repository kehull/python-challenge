#import the os and document
import os
import csv
# Path to collect data from the Resources folder
bank_csv = os.path.join( 'Resources', 'budget_data.csv')

#define the summary function, which will iterate through csvreader
def summary(csvreader):
    #establish variables with global scope outside of the loop
    Total_Months = 0
    Total = 0
    Changes = []
    Difference = []
    Greatest_Increase = 0
    Greatest_Decrease = 0
    Avg_Change = 0
    
    #begin loop
    for row in csvreader:
        #give the columns of the csv variable names to make them easier to call on later
        date = str(row[0])
        money = int(row[1])
        Total_Months += 1 #+1 to Total_Months per row
        Total = Total + money # add value from money to Total per row
        Changes.append(money) #put profits/losses into Changes list
        if len(Changes)>=2: #make sure there are enough items in the Changes list to perform the math functions inside of this if statement
            Difference.append(Changes[-1] - Changes[-2]) #calculate the difference between the current month's profit/loss and the previous month's; append that value to Difference list
        if len(Difference)>=1: #make sure there are enough items in the Difference list to perform the math functions inside of this if statement
            if Difference[-1] > Greatest_Increase and Difference[-1] > 0: #compare the current Difference value to the largest Difference value thus far to determine if the new value is greater. Lesser values can't possibly be the greatest value, so those are ignored. 
                Greatest_Increase = Difference[-1]  #reset the previous value to the greater value
                Greatest_Increase_Date = (row[0]) #store the date from the current row as a variable so it can be called later in a print statement
            if abs(Difference[-1]) > abs(Greatest_Decrease) and Difference[-1] < 0: #compare the absolute value of the current Difference value to the largest Difference value thus far to determine if the new value is greater.
                Greatest_Decrease = Difference[-1] #reset the previous value to the greater value
                Greatest_Decrease_Date = (row[0]) #store the date from the current row as a variable so it can be called later in a print statement
        if len(Difference)>=2: #make sure therea re enought items in the Difference list to perform the math functions inside of this if statement
            Avg_Change = sum(Difference)/len(Difference) #perform calculation to determine the average change from month to month
#create summary table and output as a txt file
    output_path = os.path.join("Analysis", "pybank_summary.txt") #path for where to save the document
    with open (output_path,'w', newline='') as datafile:
        writer = csv.writer(datafile)
        writer.writerow([(f"Financial Analysis")])
        writer.writerow([(f"----------------------------")])
        writer.writerow([(f"Total Months: {Total_Months}")])
        writer.writerow([(f"Total: ${Total}")])
        writer.writerow([(f"Average Change: ${str(round(Avg_Change,2))}")])
        writer.writerow([(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})")])
        writer.writerow([(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})")])
    print(writer)
   
#open the pybank_summary.txt file and read it into the terminal
file = os.path.join("Analysis", "pybank_summary.txt")#path to find the document
with open(file, 'r') as text:
    print(text)
    lines = text.read()
    print(lines)


