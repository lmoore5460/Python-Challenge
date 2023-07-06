import csv

# Read the CSV file
with open('/Users/Repository/PyBank/Resources/budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row

    #variables
    total_months = 0
    net_total = 0
    previous_profit = 0
    profit_changes = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]

    # Iterate over each row in the dataset
    for row in csvreader:
        # Extract the date and profit/loss values
        date = row[0]
        profit = int(row[1])

        # Calculate total months and net
        total_months += 1
        net_total += profit

        #profit change
        if total_months > 1:
            change = profit - previous_profit
            profit_changes.append(change)

            # Check for greatest increase/decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        previous_profit = profit

# Calculate the average change
average_change = sum(profit_changes) / len(profit_changes)

# Prepare the output string
output = "Financial Analysis\n"
output += "-----------------------------\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${net_total}\n"
output += f"Average Change: ${average_change:.2f}\n"
output += f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
output += f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

# Write the output to a text file
with open('financial_analysis_output.txt', 'w') as output_file:
    output_file.write(output)

print("Analysis completed. Results exported to financial_analysis_output.txt.")
