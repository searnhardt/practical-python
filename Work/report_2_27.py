# report.py
#
# Exercise 2.7
'''
Tie all of this work together by adding a few additional statements to your `report.py` program 
that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and 
the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio
along with the gain/loss.
'''
import csv
import sys

portfolio = []
#holding = {} # Initial empty dict

def read_prices(filename2):
    #exercise 2.6
    pricesfn = {}
    f = open(filename2, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            pricesfn[row[0]] = float(row[1])
        except:
            pass
    return pricesfn

def read_portfolio(filename):
    #Exercise 2.5
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
                    print(holding)
                    portfolio.append(holding)
                    #print(portfolio)
            except:
                print('Bad line found and skipped')
                next(f)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    filename2 = 'Data/prices.csv'

cost = read_portfolio(filename)  #List
prices = read_prices(filename2)  #Dictionary
#print('Total cost', cost)
print("")
#print('Prices', prices)
'''
{'name': 'AA', 'shares': 100, 'price': 32.2}
dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
for dic in dataList:
    for key in dic:
        print(dic[key])
'''
for stock in cost:
    for holding['name'] in stock:
        print(stock[holding])
        #for name in holding:
            #print(name)
            #print(stock[holding[1]])
