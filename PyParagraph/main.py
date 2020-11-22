import os
import csv

paragraph_file = os.path.join("Mathematicians_Lament_Section.txt")

with open(paragraph_file, "r") as text:
    lines = text.read()
    print(lines)

    Word_Count = 0
    Sentence_Count = 0
    Word_Length = 0
    Sentence_Length = 0

output_path = os.path.join("Paragraph_Analysis.txt") 
with open (output_path,'w', newline='') as datafile:
        writer = csv.writer(datafile)
        writer.writerow([("Paragraph_Analysis")])
        writer.writerow([("-------------------------")])
        writer.writerow([f'Approximate Word Count: {Word_Count}'])
        writer.writerow([f'Approximate Sentence Count: {Sentence_Count}'])
        writer.writerow([f'Average Letter Count: {Word_Length}'])
        writer.writerow([f'Average Sentence Length:{Sentence_Length}'])
        print(writer)

#open the Paragraph_Analysis.txt file and read it into the terminal
file = os.path.join("Paragraph_Analysis.txt")
with open(file, 'r') as text:
    lines = text.read()
    print(lines)