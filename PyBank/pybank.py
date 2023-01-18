import csv

input_file = "Resources/budget_data.csv"

total_month = 0
total_profit = 0
total_change = 0
total_change_month = 0

# the benchmark value is small enough to work as a bottom line
greatest_increase=["",-9999999999999]
# the benchmark value is big enough to work as a ceiling line
greatest_decrease=["",9999999999999]

with open(input_file, encoding='utf-8') as budget_data_file:
    rows = csv.reader(budget_data_file, delimiter=",")
    #print(rows) -> info of CSV file 
    next(rows)
    #x=next(rows)
    #y=next(rows)
    
    #print(x)
    #print(y)
    
    # data row
    first_row=next(rows)
    total_month+=1
    total_profit+=int(first_row[1])
    pre_profit=int(first_row[1])
    
    for row in rows:
        # total month, followed by first_row, entering for loop
        total_month += 1
        # total profit, followed by first_row, entering for loop
        total_profit += int(row[1])
        
        
        net_change=int(row[1])-pre_profit
        total_change += net_change
        # ex: from Jan to Feb, changed once, but consists of 2 months
        total_change_month += 1

        # save previous month's data, when next month comes, we have benchmark
        pre_profit = int(row[1])
        

        if (net_change>greatest_increase[1]):

            greatest_increase[1]=net_change
            greatest_increase[0]=row[0]

        if (net_change<greatest_decrease[1]):

            greatest_decrease[1]=net_change
            greatest_decrease[0]=row[0]

    
# final output
print(f"{total_month} {total_profit} {total_change/total_change_month}")
print(f"{greatest_increase[0]} (${greatest_increase[1]})")
print(f"{greatest_decrease[0]} (${greatest_decrease[1]})")
    


output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: ${total_change/total_change_month:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

print (output)

with open("analysis/pybank_output.txt", "w") as txt_file:
    txt_file.write(output)



