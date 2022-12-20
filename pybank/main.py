# Import modules
import os
import csv

# Reference csv file with bank data to analyze
pl_data = os.path.join("resources", "budget_data.csv")

# Set row count (month count) variable and initialize, make list for months
monthcount = 0
months = []

# Open csv data file, iterate through file to count each month (row) - be sure to exclude header. Also append months to a list
with open(pl_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        monthcount+= 1 
        months.append(row[0])

# print header and line break for data readout (formatting)
print("Financial Analysis")
print("-----------------------------")

# print result (total number of months)
print("Total Months: " + str(monthcount))

# Create and initialize variable for "net total profit/loss", create list to store monthly P/L
netpl = 0
pl = []

# Open csv data file, iterate through file to sum each month's P/L. Also create list of P/L to use for further calcs
with open(pl_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        netpl+= int(row[1])
        pl.append(int(row[1]))

# print result (total sum of P/L)
print("Total: $" + str(netpl))

    
#Create a list to store monthly change in P/L
monthlychange = []

# Open csv data file, iterate through profit list to calculate monthly change (subtract 1 from range b.c. the first month will not have associated change)
with open(pl_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in range(len(pl)-1):
        monthlychange.append(pl[row+1]-pl[row])

# Calculate and print average change 
print(f"Average Change: {round(sum(monthlychange)/len(monthlychange),2)}")

# Determine which month had the greatest increase and decrease in profit
max_increase = max(monthlychange)
max_decrease = min(monthlychange)

# Determine which 2 months have the max increase and max decrease, adjust the index to output the "new month" involved in difference
max_inc_month = monthlychange.index(max(monthlychange)) + 1
max_dec_month = monthlychange.index(min(monthlychange)) + 1

# Print greatest inc and greatest dec months & amounts
print(f"Greatest Increase in Profits: {months[max_inc_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {months[max_dec_month]} (${(str(max_decrease))})")

# Output to csv file
output_path = os.path.join("analysis", "pybank_analysis.txt")
with open(output_path, "w") as txt:
    txt.write("Fianancial Analysis")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write("Total Months: " + str(monthcount))
    txt.write("\n")
    txt.write("Total: $" + str(netpl))
    txt.write("\n")
    txt.write(f"Average Change: {round(sum(monthlychange)/len(monthlychange),2)}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: {months[max_inc_month]} (${(str(max_increase))})")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: {months[max_dec_month]} (${(str(max_decrease))})")



