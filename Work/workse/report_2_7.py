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
curvalue = 0.00
#holding = {} # Initial empty dict

def read_prices(filename2):
    #exercise 2.6 - Dictionary
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
    #Exercise 2.5 - List of Dictionaries
    with open(filename, 'rt') as f:
        #portfolio = []
        #holding = {} # Initial empty dict
        reader = csv.reader(f)
        #rows = csv.reader(f)
        headers = next(reader)
        #print("Holdings")
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
    filename2 = 'Work/Data/prices.csv'

share = read_portfolio(filename)  #List
prices = read_prices(filename2)  #Dictionary
#print('Total cost', cost)
#print("")
#print('Prices', prices)
'''
{'name': 'AA', 'shares': 100, 'price': 32.2}
dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
for dic in dataList:
    for key in dic:
        print(dic[key])
'''
#Good Code for prices
# for price in prices.items():
#    print(price[1])

for stock in share:
    print("Stock Name: ",stock['name'],"   Shares: ",stock['shares'],"   Initial Price: ",format(stock['price'],'.2f'))
    #print(stock['shares'])
    #print(stock['price'])
    inicost = stock['shares'] * stock['price']
    print("Initial Purchase Cost: ",format(inicost,'.2f'))
    for price in prices.items():
        if stock['name'] == price[0]:
            #print(price[0])
            print("Current Price: ",format(price[1],'.2f'))
            curcost = stock['shares'] * price[1]
            if curcost > inicost:
                print("gain of ",format(curcost - inicost,'.2f'))
            else:
                print("loss of ",format(inicost - curcost,'.2f'))
            curvalue += curcost
            print("")
print("Current Portfolio Value is ",format(curvalue,'.2f'))
    #    print(stock[st_name])

#print(share) # list of dictionaries
#print("")
#print(prices)