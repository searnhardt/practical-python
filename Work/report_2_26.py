# report.py
#
# Exercise 2.26
import csv

def read_prices(filename):
    prices = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        prices[row0] = float([row1])
    return prices

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
