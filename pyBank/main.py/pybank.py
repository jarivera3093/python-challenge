# Bring in libraries
import os
import csv

# Get the current directory
current_dir = os.getcwd()
# The file name
csvpath = 'budget_data.csv'
# Join together the path and the file name (EX: C://project/budget_data.csv)
ospath = os.path.join(current_dir,csvpath)

# Open file and save it as the variable "csvfile"
with open (csvpath, encoding='UTF-8') as csvfile:
    # Make a variable "csvreader" and set it to the csv
    csvreader = csv.reader(csvfile, delimiter=',')
    # Move to the next row, so that we skip the column header
next(csvreader)
# Setup variables to default state
totalMonths = 0
totalRevenue = 0
revenueChange = 0
revenue = []
previousRevenue = 0
revenueChange_list = ["row 1"]

    
    # Go through every row in csvreader
for row in csvreader:
        print('ROW ',type(row))
        print(row)
        continue
        # Add 1 to months for each row as each row is a new month
        totalMonths += 1
        # Add the profit/loss from each row to total
        # "int" forces it to be an interger, row is the current row, and [1] takes the data in the 1st(2nd) column
        totalRevenue += int(row[1])
        # calculate monthly revenue changes and establish previous revenue, 
        revenueChange = int(row[1]) - previousRevenue
        previousRevenue = int(row[1])
        revenueChange_list = revenueChange_list - [revenueChange]

    # Print all the data in a nice way
    # f"" makes it so we can have variables in the print, with the variable being in curly brackets
        print("Financial Analysis")
        print(f"Total Months: {totalMonths}")
        print(f"Total: {totalRevenue}")


    
     
