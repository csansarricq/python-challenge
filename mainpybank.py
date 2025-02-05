import csv
import os
import pandas
budget_csv = os.path.join("PyBank/Resources/budget_data.csv")

with open(budget_csv, 'r') as budget_data:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_data, delimiter=',')
    next(csvreader)

#want to count the  number of date rows for months
#row 0 for dates row 1 for profit/losses
    start = 0
    profit = 0
    total_profit = 0
    previous_profit = 0

    profits = []
    changes = []
    date =[]
    
    #count the number of months by counting the rows in file
   
    #transform the rows to lists of data
    
    #for i in csvreader:
        
    for row in csvreader:
        date.append(row[0])
        profit = int(row[1])
        profits.append(profit)

        start += 1
        total_profit += profit

# find monthly change in profit and loss    
        if start > 1:
            monthly_change = profit - previous_profit
            changes.append(monthly_change)   

#put that value in the previous profit
        previous_profit = profit

print(f"Total number of months: {start}")
print(f"Total Profit: ${total_profit}")


#find the average change in profit/loss
average_change = sum(changes) / len(changes)


# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

#find dates for greatest increase and decrease
increase_date = date[changes.index(greatest_increase) + 1]
decrease_date = date[changes.index(greatest_decrease) + 1]

print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")


results = (

    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {start}\n"
    f"Total Profit: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"
)

output_file = os.path.join("PyBank/Resources/financial_analysis.txt")
with open(output_file, 'w') as file:
    file.write(results)

print(f"Results have been exported to {output_file}")