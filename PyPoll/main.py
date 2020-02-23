import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")

# Lists to store data
votes = []
candidates = []

# Open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csvfile)

    for row in csvreader:
        # Add votes
        votes.append(int(row[0]))
        # Add candidates
        candidates.append(row[2])

        #Get total votes
        total_votes = sum(votes)

        # Create list of unique candidates
        unique_list = []
        for name in candidates:
            if name not in unique_list:
                unique_list.append(name)
        
        # Get votes for each candidate
        def cadidate_votes(candidate):
            for candidate in unique_list:
                candidate_total = 0
                if row[2] == candidate:
                    candidate_total = candidate_total + int(row[0])
                return candidate_total

    # Print analysis to terminal
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {str(total_votes)}')
    print("-----------------------")
    print(f'{str(unique_list)}')

# Export text file with results