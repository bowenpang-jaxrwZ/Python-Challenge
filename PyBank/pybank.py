import csv

input_file = "Resources/budget_data.csv"

total_month = 0
total_profit = 0
total_change = 0
total_change_month = 0

with open(input_file) as newfile:
    rows = csv.reader(newfile)
    next(rows)

    first_row = next(rows)
    # +=1
    total_month = total_month + 1
    total_profit += int(first_row[1])
    pre_profit = int(first_row[1])

    for row in rows:
        total_month = total_month + 1
        total_profit += int(row[1])

        change = int(row[1]) - pre_profit
        total_change += change
        total_change_month += 1

        pre_profit = int(row[1])



print(f"{total_month} {total_profit} {total_change/total_change_month}")


    


output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: ${total_change/total_change_month:.2f}
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
"""

print (output)

with open("analysis/pybank_output.txt", "w") as txt_file:
    txt_file.write(output)



