# report.py
#
# Exercise 2.4
import csv
import sys

portfolio = []
#holding = {} # Initial empty dict

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        #portfolio = []
        #holding = {} # Initial empty dict
        reader = csv.reader(f)
        #rows = csv.reader(f)
        headers = next(reader)
        for row in reader:
            holding = {}
            try:
                #for row in reader:
                    #holding = (row[0], int(row[1]), float(row[2]))
                    #portfolio.append(holding)
                #for line in f:
                    #row = line.split(',')
                    #holdings[row[0]] = float(row[1])
                    #name, shares, price = row
                    #print(row)
                    holding['name'] = row[0]
                    holding['shares'] = int(row[1])
                    holding['price'] = float(row[2])
                    #print(holding)
                    portfolio.append(holding)
                    #print(portfolio)
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