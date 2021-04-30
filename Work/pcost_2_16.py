# pcost.py
#
# Exercise 2.16
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    row_total = 0
    with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            # row = next(rows)
            for rowno, row in enumerate(rows, start=1):
                record = dict(zip(headers,row))
                try:
                    nshares = int(record['shares'])
                    price = float(record['price'])
                    total_cost += nshares * price
                # This catches errors in int() and float() conversions above
                except ValueError:
                    print(f"Row {rowno}: Bad row: {row}")
                    #next(f)
    return(round(total_cost,2))

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)