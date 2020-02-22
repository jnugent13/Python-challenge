import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")

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
        profit.append(int(row[1]))

        # Get total months listed in dataset
        months_count = len(date)

        # Net total of profit and losses over time period
        total_profit = sum(profit)

        # Profit change over period
        profit_change = [j-i for i, j in zip(profit[:-1], profit[1:])]
        profit_change.insert(0,0)
        total_change = sum(profit_change)

        # Average in changes of profit and losses over time period
        def average(profit_change):
            length = len(profit_change) - 1
            return '${:,.2f}'.format(total_change / length)
        
        # Greatest increase in profits (date and amount) over time period
        def greatest_increase(profit_change):
            greatest_value = max(profit_change)
            n = profit_change.index(greatest_value)
            return str(date[n]) + " ($" + str(greatest_value) + ")"

        # Greatest decrease in losses (date and amount) over time period
        def greatest_decrease(profit_change):
            greatest_loss = min(profit_change)
            n = profit_change.index(greatest_loss)
            return str(date[n]) + " ($" + str(greatest_loss) + ")"

    # Print analysis to terminal
    print('Financial Analysis')
    print('-----------------------------------')
    print(f'Total Months: {str(months_count)}')
    print(f'Total: ${str(total_profit)}')
    print(f'Average Change: ${str(average(profit_change))}')
    print(f'Greatest Increase in Profit: {str(greatest_increase(profit_change))}')
    print(f'Greatest Decrease in Profit: {str(greatest_decrease(profit_change))}')

# Export text file with results 
output_file = os.path.join("Output", "budget_results.csv")

with open(output_file,"w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Create headers
    csvwriter.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profit", "Greatest Decrease in Profit"])
    csvwriter.writerow([str(months_count), "$" + str(total_profit), "$" + str(average(profit_change)), str(greatest_increase(profit_change)), str(greatest_decrease(profit_change))])

