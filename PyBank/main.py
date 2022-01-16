import csv

csvpath = "budget_data.csv"

totalMonths = 0
totalProfit = 0

changes = []
changeMonths = []
previousProfit = 0

with open(csvpath, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
        totalMonths += 1
        totalProfit += int(row[1])

        # if not first row, then change
        if totalMonths > 1:
            change = int(row[1]) - previousProfit
            changes.append(change)
            changeMonths.append(row[0])

    #update previous profit
        previousProfit = int(row[1])

    print(row)

print(totalMonths)
print(totalProfit)
avg_change = (sum(changes) / len(changes))
max_change = max(changes)
min_change = min(changes)
print(max_change)
print(min_change)


maxMonth_idx = changes.index(max(changes))
maxMonth = changeMonths[maxMonth_idx]
#print(changeMonths)
minMonth_idx = changes.index(min(changes))
minMonth = changeMonths[minMonth_idx]

print(maxMonth)
print(minMonth)
print()

#Creates Summary
summary = f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalProfit}
Average  Change: ${avg_change}
Greatest Increase in Profits: {maxMonth} (${max_change})
Greatest Decrease in Profits: {minMonth} (${min_change})
"""
print(summary)

#writes text file
with open("analysis.txt", "w") as file:
    file.write(summary)

