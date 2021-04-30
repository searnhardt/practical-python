# pcost.py
#
# Exercise 2.15
import csv
import sys

def portfolio_cost(filename):
    total = 0
    row_total = 0
    with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for rowno, row in enumerate(rows, start=1):
                try:
                    #print(rownum)
                    row_total = int(row[1]) * float(row[2])
                    total += row_total
                except ValueError:
                    print(f"Row {rowno}: Couldn't convert: {row}")
                    #next(f)
    return(round(total,2))

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)