#PyBank

import os
import csv
import sys

#file path
budget_data_csvfile = os.path.join('..', 'Resources', 'budget_data.csv')


def data_calc(rowdata):

    #month list         =   Colume 1 (from data set) 
    #profit/loss list   =   Colume 2 (from data set)
    #profit_difference list = profit/loss(row + 1) - profit/loss(row)  
    months_list = []
    profit_loss_list = []
    profit_difference = []



    #temperory variable = 0, and boolean = true
    profit_diff_temp = 0
    first_row = True
    


    #sets first row to 0 in profit_difference list
    profit_difference.append(0)




    #sets values from each column in data set to its respective list
    for a,b in rowdata:
        months_list.append(str(a))
        profit_loss_list.append(int(b))
        
        #figures out the difference in profit month to month
        if not first_row:
            profit_difference.append(int(b)  - int(profit_diff_temp))
            
        else:
            first_row = False

        profit_diff_temp = b    

 
 
    #-----------------tasks-----------------------------------------
    # --------------------------------------------------------------  
    print('Finalcial Analysis')
    print('----------------------------')

    #The total number of months included in the dataset
    total_months = len(months_list)
    print(f'Total Months: {total_months}')

    #The net total amount of "Profit/Losses" over the entire period
    net_total = sum(profit_loss_list)
    print(f'Net Total: ${net_total}')

    #The average of the changes in "Profit/Losses" over the entire period
    totalAverage_change = round((sum(profit_difference) / (total_months - 1)),2)
    print(f'Average: ${totalAverage_change}')
    
    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase =  max(profit_difference)
    x = profit_difference.index(int(greatest_increase))
    print(f'Greatest Increase in Profits: {months_list[x]}  (${greatest_increase})')
    
    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease  = min(profit_difference)
    y = profit_difference.index(int(greatest_decrease))
    print(f'Greatest Decrease in Profits: {months_list[y]}  (${greatest_decrease})')







    #outputs the data into txt file
    with open("Pybank_output.txt", "w") as f:
        sys.stdout = f # Change the standard output to the file we created.
        
        print('Finalcial Analysis')
        print('----------------------------')
        print(f'Total Months: {total_months}')
        print(f'Net Total: ${net_total}')
        print(f'Average: ${totalAverage_change}')
        print(f'Greatest Increase in Profits: {months_list[x]}  (${greatest_increase})')
        print(f'Greatest Decrease in Profits: {months_list[y]}  (${greatest_decrease})')
        
        stdoutOrigin = sys.stdout # Reset the standard output to its original value











#opens files, sets delimiters, and passes data into 'data_calc' function
with open(budget_data_csvfile, 'r') as csvfile:    

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    data_calc(csvreader)

   
