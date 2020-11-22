import os
import csv
import re

#open the file and read it in
paragraph_file = os.path.join("Mathematicians_Lament_Section.txt")
with open(paragraph_file, "r") as text:
    lines = text.read()

    #do the calculations
    Word_Count = int(len(lines.split())) #This is not a perfect way to count words- for example, it counts hyphenated words and phrases as single words, which could be an issue if you want a phrase such as "well-to-do" to count as three words. However, in most cases it works fine as an approximation.
    Sentence_Count = int(len(lines.split("(?<=[.!?]) +"))) #This is not a perfect way to count sentences- for example, it would count a sentence like "The planet closest to the sun (ie Mercury) has the most extreme temperature variations." as three separate sentences. However, in most cases it works fine as an approximation.
    Sentence_Length = round((Word_Count/Sentence_Count),1)
    All_Letters = int(len(re.sub("(?<=[.!?]) +", '', str(lines)))) #This code removes all characters listed in the first argument of re.sub() from the text and returns the remaining characters as items a list, then returns the length of that list.
    Word_Length = round((All_Letters/Word_Count),1)

#write summary table. The assignment did not specify do do this, so it may not be necessary, but I wanted more practice using this method.
output_path = os.path.join("Paragraph_Analysis.txt") 
with open (output_path,'w', newline='') as datafile:
        writer = csv.writer(datafile)
        writer.writerow([("Paragraph_Analysis")])
        writer.writerow([("-------------------------")])
        writer.writerow([f'Approximate Word Count: {Word_Count}'])
        writer.writerow([f'Approximate Sentence Count: {Sentence_Count}'])
        writer.writerow([f'Average Letter Count: {Word_Length}'])
        writer.writerow([f'Average Sentence Length: {Sentence_Length}'])
        print(writer)

#open the Paragraph_Analysis.txt file and read it into the terminal
file = os.path.join("Paragraph_Analysis.txt")
with open(file, 'r') as text:
    lines = text.read()
    print(lines)