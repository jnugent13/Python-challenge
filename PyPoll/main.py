import csv
import os

csvpath = os.path.join("..", "Resources", "election_data.csv")

votes = []
candidates = []

# Open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header first
    csvheader = next(csvfile)
    
    for row in csvreader:
        # Add votes
        votes.append(row[0])

        # Get list of candidates who received votes
        candidates.append(row[0])

        # Get total number of votes cast
        total_votes = len(votes)

        print(total_votes)
