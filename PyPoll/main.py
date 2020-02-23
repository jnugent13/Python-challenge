import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")

# Lists to store data
votes = []
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvpath, delimiter=",")

    # Skip the header
    header = next(csvfile)

    for row in csvreader:
        # Add votes
        votes.append(int(row[0]))
        # Add candidates
        candidates.append(str(row[0]))

        #Get total votes
        total_votes = sum(votes)

        # Create list of unique candidates
        def unique(candidates):
            unique_list = []
            for name in candidates:
                if name not in unique_list:
                    unique_list.append(name)
            return unique_list
        
        # Get votes for each candidate
        def cadidate_votes(candidate):
            for candidate in candidates:
                candidate_total = 0
                if row[2] == candidate:
                    candidate_total = candidate_total + int(row[0])
                return candidate_total


    # Print analysis to terminal
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {str(total_votes)}')
    print("-----------------------")


# Export text file with results