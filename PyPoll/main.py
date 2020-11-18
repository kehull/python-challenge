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
        #Code works fine up to here, then the for loop counts rows instead of occurances for some reason. It only counts all the rows for the first list item, then slightly fewer for the other items. Very weird.
        for x in Candidates:
            if x in Votes_Per:
                Votes_Per[x] +=1
            else:
                Votes_Per[x] = 1

        

        
    
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {Total_Votes}')
    print("-------------------------")
    print (Candidates)
    print(Votes_Per)


            

