import csv
import os

csvpath = os.path.join("git/Python-challenge/Resources/budget_data.csv")

# Lists to store data
date = []
profit = []

# Open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add date
        date.append(row[1])
        # Add profit/loss
        profit.append(row[2])

        # Get total months listed in dataset
        def total_months(date):
            months_count = len(date)
            return months_count

        # Net total of profit and losses over time period
        def total_profit(profit):
            total = sum(profit)
            return total

        # Average in changes of profit and losses over time period
        def average(profit):
            length = len(profit)
            total = sum(profit)
            return total / length

        # Greatest increase in profits (date and amount) over time period
        def greatest_increase(profit):
            greatest_profit = max(profit)
            return greatest_profit

        # Greatest decrease in losses (date and amount) over time period
        def greatest_decrease(profit):
            greatest_loss = min(profit)
            return greatest_loss

        # Print analysis to terminal
        print('Financial Analysis')
        print('-----------------------------------')
        print(f'Total Months: {str(total_months(date))}')
        print(f'Total: ${str(total_profit(profit))}')
        print(f'Average Change: ${str(average(profit))}')
        print(f'Greatest Increase in Profits: ${str(greatest_increase(profit))}')
        print(f'Greatest Decrease in Profit: ${str(greatest_decrease(profit))}')

        # Export text file with results 