import csv
import os

csvpath = os.path.join("git/Python-challenge/Resources/budget_data.csv")

# Open the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    # Define variables for values
    def print_values(budget_data):
        month = str(budget_data[0])
        profit = int(budget_data[1])

        # Calculate number of months in dataset
        month_list = []
        for row in csvreader:
            month_list.append(month)
            return len(month_list)

        # Net total of profit and losses over time period
    # Average in changes of profit and losses over time period

    # Greatest increase in profits (date and amount) over time period

    # Greatest decrease in losses (date and amount) over time period

    # Print analysis to terminal
    print(print_values(budget_data=csvreader))

    # Export text file with results 