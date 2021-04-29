# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total = 0
    row_total = 0
    with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            try:
                for row in rows:
                    #print(line, end='')
                    #t = line.replace('\n','')
                    #row = t.split(',')
                    #row[2] = row[2].delete(-2)
                    #print(row[2])
                    row_total = int(row[1]) * float(row[2])
                    total += row_total
            except:
                print('Bad line found and skipped')
                next(f)
    #print('Total cost', round(total,2))
    return(round(total,2))

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)