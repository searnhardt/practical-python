# report.py
#
# Exercise 2.4
import csv
import sys

portfolio = []

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
        except:
            print('Bad line found and skipped')
            next(f)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = read_portfolio(filename)
print('Total cost', cost)