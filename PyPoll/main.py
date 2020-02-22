import csv
import os

csvpath = os.path.join("Downloads", "election_data.csv")

# Lists to store data
votes = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvpath, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        # Create function to print values
        def print_results(election_data):
            vote = int(election_data[0])
            votes.append(vote)
            total_votes = sum(votes)
            return total


            # Print analysis to terminal
            print("Election Results")
            print("-----------------------")
            print("Total Votes: " + total_votes)

# Export text file with results