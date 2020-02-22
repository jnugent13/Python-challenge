import csv
import os

csvpath = os.path.join("Downloads", "election_data.csv")

# Lists to store data
votes = []
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvpath, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        # Add votes
        votes.append(row[0])
        # Add candidates
        candidates.append(row[1])

        #Get total votes
        total_votes = sum(votes)

        # Create list of unique candidates
        def unique(candidates):
            unique_list = []
            for name in candidates:
                if name not in unique_list:
                    unique_list.append(name)
            

    # Print analysis to terminal
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {str(total_votes)}')
    print("-----------------------")


# Export text file with results