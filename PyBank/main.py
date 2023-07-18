# import libraries 
import csv
import os

# set file path to csv and txt files
csvpath = os.path.join("resources\\budget_data.csv")
analysis = os.path.join("analysis\\analysis.txt")


# set variables
total_months = 0
profit_loss = []
total_amount = 0
prev_year_list = []
greatest_increase=["",-1000]
greatest_decrease = ["", 999999]

# open file
with open(csvpath) as csvfile:
     
    csvreader = csv.reader(csvfile, delimiter = ",")

    # skip the header row and first row
    csvheader = next(csvreader)
    first_row = next(csvreader)
    prev_year = int(first_row[1])
    total_months = total_months + 1
    total_amount = total_amount + int(first_row[1])
    
    # loop through to find total months and total amount
    for row in csvreader:
       total_months = total_months + 1
       total_amount = total_amount + int(row[1])

       # Calculating change over a period
       profit_loss.append(int(row[1]))
       change=int(row[1])-prev_year
       prev_year_list.append(change)
       prev_year=int(row[1])

       # Calculating greatest increase and greatest decrease
       if change > greatest_increase[1]:
           greatest_increase[0]=row[0]
           greatest_increase[1]=change
       if change < greatest_decrease[1]:
           greatest_decrease[0]=row[0]
           greatest_decrease[1]=change

    # Calculate average change
    avg = sum(prev_year_list)/len(prev_year_list)
    
    # round the average
    avg = round(avg,2)
       

# write the result to a text file.
with open(analysis,"a") as txtfile:
    txtfile.write(f"Financial Analysis\n"
                  f"------------------------\n"
                  f"Total months : {(total_months)} \n" 
                  f"Total : ${total_amount} \n"
                  f"Average Change : ${avg} \n"
                  f"Greatest Increase in Porfits: {greatest_increase[0]}, (${greatest_increase[1]}) \n"
                  f"Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]}) "
                  )
    
    #print results 
    print(f"Total months :{total_months} \n")
    print(f"Total: ${total_amount} \n")
    print(f"Average change : ${avg} \n")
    print(f"Greatest Increase in Porfits: {greatest_increase[0]}, (${greatest_increase[1]}) \n")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})")
