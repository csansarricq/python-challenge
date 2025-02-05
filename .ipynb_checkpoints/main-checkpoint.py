import csv
import os
budget_csv = r"OneDrive/Desktop/Module_3/PyBank/Resources/budget_data.csv"

with open(budget_csv) as budget_data:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_data, delimiter=',')
    print(csvreader)
