#import the os and document
import os
import csv
# Path to collect data from the Resources folder
election_csv = os.path.join( 'Resources', 'election_data.csv')

with open(election_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

#def summary(csvreader):
    #establish variables with global scope outside of the loop
    Total_Votes = 0
    Candidates = []
    Votes_Per = {}
    
#begin loop
    for row in csvreader:
        Voter_ID = str(row[0])
        Country = str(row[1])
        Contender = str(row[2])
        Total_Votes += 1 #+1 to Total_Voters per row
        if Contender not in Candidates:
            Candidates.append(Contender)
        if Contender in Votes_Per:
            Votes_Per[Contender] +=1
        else:
            Votes_Per[Contender] = 1
#create summary table and output as a txt file
    output_path = os.path.join("Analysis", "pypoll_summary.txt") #path for where to save the document
    with open (output_path,'w', newline='') as datafile:
        writer = csv.writer(datafile)
        writer.writerow([("Election Results")])
        writer.writerow([("-------------------------")])
        writer.writerow([(f'Total Votes: {Total_Votes}')])
        writer.writerow([("-------------------------")])
        for key, value in Votes_Per.items():
            Vote_Percent = (float(value)/float(Total_Votes))*100
            writer.writerow([(f'{key}: {Vote_Percent:.3f}% ({value})')]) 
        Winner = [key for key in Votes_Per.keys() if Votes_Per[key] == max(Votes_Per.values())] #this was a great line of code I found on a Stack Overflow discussion here: https://stackoverflow.com/a/62152615/14266631 . When the max() function is used, if there are multiple items with that same value, unless you tell it otherwise, Python will return the single value that it encountered first. This can be problematic in some cases, as it may be relevant that multiple items share the max value. This line of code iterates through a dictionary to find all key-value pairs with values matching the maximum value and outputs those pairs to a list. This way, if there is more than one item with the maximum value, you as the programmer have an opportunity to see the full list of items with that value. Before finishing this code, I printed the list, and it showed only one value, so I didn't have to make a decision. However, I think this function could be useful for the future.
        writer.writerow([("-------------------------")])
        writer.writerow([(f'Winner: {Winner[0]}')]) #Because the varaible Winner is actually a list, I had to call [0] to print the string properly.
        writer.writerow([("-------------------------")])
        print(writer)
   
#open the pybank_summary.txt file and read it into the terminal
file = os.path.join("Analysis", "pypoll_summary.txt")#path to find the document
with open(file, 'r') as text:
    print(text)
    lines = text.read()
    print(lines)