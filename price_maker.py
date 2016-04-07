import random as rnd
numStocks = 5

for x in range(numStocks):
    price = (rnd.randint(10 ,20))

stockList = []
stockList.append(Stock("American Broadcasting Corp", "ABC", price, 10))
stockList.append(Stock("Diversified Energy Force", "DEF", price, 12))
stockList.append(Stock("Global Health Inc", "GHI", price, 14))
stockList.append(Stock("Jasmine Kiloton LLC", "JKL", price, 16))
stockList.append(Stock("Minnesota Natural Order", "MNO", price, 18))

print()
for stock in stockList:
    print("  ", stock.name, stock.ticker, stock.starting_price)