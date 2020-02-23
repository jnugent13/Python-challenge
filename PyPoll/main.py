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
        vote_totals = []
        for candidate in unique_list:
            candidate_total = 0
            if row[2] == candidate:
                candidate_total = candidate_total + int(row[0])
            vote_totals.append(candidate_total)

    # Print analysis to terminal
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {str(total_votes)}')
    print("-----------------------")
    print(f'{str(unique_list)}: {str(vote_totals)}')

# Export text file with results
output_file = os.path.join("Output", "election_results.csv")

with open(output_file, "w") as csvfile:
    csvwriter = csv.writer(output_file, delimiter=",")

    #Create headers
    csvwriter.writerow(["Total", unique_list])
    csvwriter.writerow([str(total_votes), str(vote_totals)])