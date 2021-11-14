#The data we need to retrieve
#1. The total number of votes cast
#2. A Complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of voted each candidate won
#5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:

    #To do: read and analyize the data here
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)




