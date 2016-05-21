import random as rnd

stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
prices = []

for x in range(len(stocks)):
    prices.append(rnd.randint(10, 20))

market = dict(zip(stocks, prices))

print(market)