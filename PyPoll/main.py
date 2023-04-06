#Import dependencies
import os, csv
from decimal import *

#Variables
c = []
d = []
r = []
t = []
#Reading CSV File

csvpath = 'Challenges/03_Python_Challenge/python-challenge/PyPoll/Resources/election_data.csv'
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
        t.append(row[0])
        if row[2] == 'Charles Casper Stockham':
            c.append(row[0])
        elif row[2] == 'Diana DeGette':
            d.append(row[0])
        elif row[2] == 'Raymon Anthony Doane':
            r.append(row[0])
        else: 
            print('Null Value')


#Calculations
#Total Calc
total_votes = len(t)
c_total = len(c)
d_total = len(d)
r_total = len(r)

#Create dict to determine winnner
w_dict = dict([('Charles Casper Stockham', c_total),('Diana DeGette', d_total),('Raymon Anthony Doane', r_total)])

#Percent Calc
per_c = (c_total/total_votes)*100
per_d = (d_total/total_votes)*100
per_r = (r_total/total_votes)*100
per_c = Decimal(per_c).quantize(Decimal('1.000'))
per_d = Decimal(per_d).quantize(Decimal('1.000'))
per_r = Decimal(per_r).quantize(Decimal('1.000'))

#Determine Winner
winner = max(w_dict, key=w_dict.get)

#Print on Terminal
print('Election Results\n')
print('----------------------------\n')
print(f'Total Votes: {total_votes}\n')
print('----------------------------\n')
print(f'Charles Casper Stockham: {per_c}% ({c_total})\n')
print(f'Diana DeGette: {per_d}% ({d_total})\n')
print(f'Raymon Anthony Doane: {per_r}% ({r_total})\n')
print('----------------------------\n')
print(f'Winner: {winner}\n')

#Writing analysis.txt file
try:
    with open(txtpath, 'w') as f:
        f.write('Election Results\n')
        f.write('----------------------------\n')
        f.write(f'Total Votes: {total_votes}\n')
        f.write('----------------------------\n')
        f.write(f'Charles Casper Stockham: {per_c}% ({c_total})\n')
        f.write(f'Diana DeGette: {per_d}% ({d_total})\n')
        f.write(f'Raymon Anthony Doane: {per_r}% ({r_total})\n')
        f.write('----------------------------\n')
        f.write(f'Winner: {winner}\n')

except FileNotFoundError:
    print("The 'analysis' directory does not exist")