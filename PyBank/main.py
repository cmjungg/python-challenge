#Import dependencies
import os, csv

#Variables
total = []
delta = []
delta_month = []
previous = 0

#Reading CSV File

csvpath = 'Challenges/03_Python_Challenge/python-challenge/PyBank/Resources/budget_data.csv'
file = 'analysis/analysis.txt'
# Specify the file to write to
dirname = os.path.dirname(__file__)
txtpath = os.path.join(dirname,file)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV READ ---> CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        x = float(row[1])
        total.append(x),
        change = x - previous
        delta.append(change)
        delta_month.append(row[0])
        previous = x

#Calculations

delta_dict = dict(zip(delta, delta_month))
delta_avg = (sum(total))/(len(total))
greatest_increase = max(delta)
greatest_decrease = min(delta)
months = len(total)
gip = delta_dict[greatest_increase]
gdp = delta_dict[greatest_decrease]

#Print analysis in terminal
print('Financial Analysis\n')
print('----------------------------\n')
print(f'Total Months: {months}\n')
print(f'Total: ${sum(total)}\n')
print(f'Average Change: ${delta_avg}\n')
print(f'Greatest Increase in Profits: {gip} ({greatest_increase})\n')
print(f'Greatest Decrease in Profits: {gdp} ({greatest_decrease})\n')

#Writing analysis.txt file
try:
    with open(txtpath, 'w') as f:
        f.write('Financial Analysis\n')
        f.write('----------------------------\n')
        f.write(f'Total Months: {months}\n')
        f.write(f'Total: ${sum(total)}\n')
        f.write(f'Average Change: ${delta_avg}\n')
        f.write(f'Greatest Increase in Profits: {gip} ({greatest_increase})\n')
        f.write(f'Greatest Decrease in Profits: {gdp} ({greatest_decrease})\n')

except FileNotFoundError:
    print("The 'analysis' directory does not exist")