# report.py
#
# Exercise 2.26
'''
line 361
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... look at the result ...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... look at the result ...
>>> 'AAPL' in prices
False
>>>
Once you have written your `read_prices()` function, test it
interactively to make sure it works:

>>> prices = read_prices('Data/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
'''
import csv
#prices = {}  #{} = dict

def read_prices(filename):
    pricesfn = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            pricesfn[row[0]] = float(row[1])
        except:
            pass
    return pricesfn
