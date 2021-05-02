# report_2_16.py  04_Sequences.md Exercist 2.16
'''
In this report, "Price" is the current share price of the stock and "Change" is the 
change in the share price from the initial purchase price.

In order to generate the above report, you’ll first want to collect all of the data 
shown in the table.  Write a function `make_report()` that takes a list of stocks 
and dictionary of prices as input and returns a list of tuples.
'''
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers,row))
            print(record)
            # stock = {
            #      'name'   : row[0],
            #      'shares' : int(row[1]),
            #      'price'   : float(row[2])
            # }
            # portfolio.append(stock)
            portfolio.append(record)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    '''
    Write a function `make_report()` that takes a list of stocks and dictionary 
    of prices as input and returns a list of tuples.
    '''
    portfolio_list = [] #list
    portfolio_line = () #tuple
    for line in portfolio:
        #print("Stock Name: ",line['name'],"   Shares: ",line['shares'],"   Initial Price: ",format(line['price'],'.2f'))
        #portfolio_line = (line['name'],line['shares'],line['price'])
        #portfolio_list.append(portfolio_line)
        #print(portfolio_line)
        for price in prices.items():
            if line['name'] == price[0]:
                #print(price[0])
                #print("Current Price: ",format(price[1],'.2f'))
                curprice = format(price[1],'.2f')
                #curprice = price[1]
                #print(curprice)
                #print(format(float(curprice) - float(line['price']),'.2f'))
                pricechange = (float(curprice) - float(line['price']))
                #portfolio_line = (line['name'],line['shares'],line['price'],pricechange)
                portfolio_line = (line['name'],line['shares'],float(curprice),pricechange)
                #print(portfolio_line)
                portfolio_list.append(portfolio_line)
                '''
                curcost = line['shares'] * price[1]
                if curcost > inicost:
                    print("gain of ",format(curcost - inicost,'.2f'))
                else:
                    print("loss of ",format(inicost - curcost,'.2f'))
                curvalue += curcost
                '''
    return portfolio_list

portfolio = read_portfolio('Work/Data/portfoliodate.csv')
prices    = read_prices('Work/Data/prices.csv')
report    = make_report(portfolio, prices)
#for r in report:
#    print('%10s %10d %10.2f %10.2f' % r)
#print("    OR")
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('-'*10,'-'*10,'-'*10,'-'*10)        
for name, shares, price, change in report:
    price = "$"+str(f'{price:.2f}')
    print(f'{name:>10s} {int(shares):>10d} {price:>10s} {change:>10.2f}')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += int(s['shares'])*float(s['price'])

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += int(s['shares'])*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)
