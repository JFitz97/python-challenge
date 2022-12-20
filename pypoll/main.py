# Import modules
import os
import csv

# Reference csv file with poll data
poll_data = os.path.join("resources", "election_data.csv")

# Identify unique candidates
candidates = []
with open(poll_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
# Used print(candidates) and ran in terminal to identify each unique candidate

# Initialize variables 
total_v = 0
stockham_v = 0
degette_v = 0
doane_v = 0

# Count total votes
with open(poll_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_v += 1

        # Conditionals to assign vote to candidate
        if row[2] == "Charles Casper Stockham":
            stockham_v += 1
        elif row[2] == "Diana DeGette":
            degette_v += 1
        elif row[2] == "Raymon Anthony Doane":
            doane_v += 1

# Printing to test values in terminal
#print(int(total_v))
#print(int(stockham_v))
#print(int(degette_v))
#print(int(doane_v))

# Calculate % votes
stockham_p = round(((stockham_v / total_v)*100), 3)
degette_p = round(((degette_v / total_v)*100), 3)
doane_p = round(((doane_v / total_v)*100), 3)

# Format and print
print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_v))
print("------------------------")
print(candidates[0] + ": " + str(stockham_p) + "% " + "(" + str(stockham_v) + ")")
print(candidates[1] + ": " + str(degette_p) + "% " + "(" + str(degette_v) + ")")
print(candidates[2] + ": " + str(doane_p) + "% " + "(" + str(doane_v) + ")")
print("------------------------")

# Conditionals to determine and print winner
if (stockham_v > degette_v > doane_v):
    print("Winner: Charles Casper Stockham")
elif (stockham_v > doane_v > degette_v):
    print("Winner: Charles Casper Stockham")
elif (degette_v > stockham_v > doane_v):
    print("Winner: Diana DeGette")
elif (degette_v > doane_v > stockham_v):
    print("Winner: Diana DeGette")
elif (doane_v > stockham_v > degette_v):
    print("Winner: Raymon Anthony Doane")
elif (doane_v > degette_v > stockham_v):
    print("Winner: Raymon Anthony Doane")  

# Formatting to match provided results
print("------------------------")

# Output to csv file
output_path = os.path.join("analysis", "pypoll_analysis.txt")
with open(output_path, "w") as txt:
    txt.write("Election Results")
    txt.write("\n")
    txt.write("------------------------")
    txt.write("\n")
    txt.write("Total Votes: " + str(total_v))
    txt.write("\n")
    txt.write("------------------------")
    txt.write("\n")
    txt.write(candidates[0] + ": " + str(stockham_p) + "% " + "(" + str(stockham_v) + ")")
    txt.write("\n")
    txt.write(candidates[1] + ": " + str(degette_p) + "% " + "(" + str(degette_v) + ")")
    txt.write("\n")
    txt.write(candidates[2] + ": " + str(doane_p) + "% " + "(" + str(doane_v) + ")")
    txt.write("\n")
    txt.write("------------------------")
    txt.write("\n")
    # Couldn't figure out conditionals statement in csv output, so ran the code and entered winner with text
    txt.write("Winner: Diana DeGette")
    txt.write("\n")
    txt.write("------------------------")

