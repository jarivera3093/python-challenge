# Bring in libraries
import os
import csv

# Get the current directory
current_dir = os.getcwd()
# The file name
csvpath = 'budget_data.csv'
# Join together the path and the file name (EX: C://project/budget_data.csv)
ospath = os.path.join(current_dir,csvpath)
#set the output of the text file
text_path = "output.txt"

# Open file and save it as the variable "csvfile"
with open (csvpath, encoding='UTF-8') as csvfile:
    csvfile.readline()
    # Make a variable "csvreader" and set it to the csv
    csvreader = csv.reader(csvfile, delimiter=',')
    # Move to the next row, so that we skip the column header
#next(csvreader)
# Setup variables to default state

    total = 0
    previous_amount = 0
    sum_delta = 0
    count = 0
    max_profit = 0
    min_profit = 999999999999
    revenueChange_list = ["row 1"]
    
    # Go through every row in csvreader
    for row in csvreader:
            count += 1
            #print(row)
            month, amount = row 
            amount = int(amount)
            total += amount
            delta = amount - previous_amount

            # if amount >= previous_amount:
            #        delta = amount - previous_amount
            # else: 
            #        delta = amount + previous_amount

            previous_amount = amount
            sum_delta += delta

            #print(delta)
            #calculate the greatest increase and greatest decrease in profit

            if delta > max_profit:
                    max_profit = delta
                    max_month = month

            if delta < min_profit:
                    min_profit = delta
                    min_month = month

    #calculate the average change = 
    next(row)
    avg_delta = sum_delta / count

    #Print the analysis
    print('Financial Analysis')
    print('-----------------------------')
    print('Total Months:', count)
    print('Total:', total)
    print('Average Change:', avg_delta)
    print(f'Greatest Increase in Profit {max_month} (${max_profit})')  
    print(f'Greatest Decrease in Profit {min_month} (${min_profit})')

    #Open a file in write mode ('w')
    with open ('text_path', 'w') as file:
        #write text to the file
        file.write("Financial Analysis")

    
    