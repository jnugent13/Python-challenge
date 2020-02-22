import csv
import os
import sys

csvpath = os.path.join("../Resources", "budget_data.csv")

# Lists to store data
date = []
profit = []

# Open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header first
    csvheader = next(csvfile)
    
    for row in csvreader:
        # Add date
        date.append(row[0])
        # Add profit/loss
        profit.append(row[1])

        # Get total months listed in dataset
        months_count = len(date)

        # Net total of profit and losses over time period
        total_profit = sum(profit)

        # Average in changes of profit and losses over time period
        def average(profit):
            length = len(profit)
            return total_profit / length

        # Greatest increase in profits (date and amount) over time period
        def greatest_increase(profit):
            greatest_profit = max(profit)
            if row[1] == greatest_profit:
                greatest_profit_date = row[0]
                return str(greatest_profit_date) + " ($" + str(greatest_profit) +")"

        # Greatest decrease in losses (date and amount) over time period
        def greatest_decrease(profit):
            greatest_loss = min(profit)
            return greatest_loss

        # Print analysis to terminal
        print('Financial Analysis')
        print('-----------------------------------')
        print(f'Total Months: {str(months_count)}')
        print(f'Total: ${str(total_profit)}')
        print(f'Average Change: ${str(average(profit))}')
        print(f'Greatest Increase in Profits: ${str(greatest_increase(profit))}')
        print(f'Greatest Decrease in Profit: ${str(greatest_decrease(profit))}')

        # Export text file with results 