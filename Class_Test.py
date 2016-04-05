import random as rnd

class Stock:
    def __init__(self, name, ticker, starting_price, current_price, volatility):
        self.name = name
        self.ticker = ticker
        self.starting_price = starting_price
        self.current_price = current_price
        self.volatility = volatility


def create_market():
    global market
    #numStocks = 5
    #for i in numStocks:
        #stock + i = Stock("")
    stock1 = Stock("ABC", "ABC", 10, 10, 1)
    stock2 = Stock("DEF", "DEF", 12, 12, 1.2)
    stock3 = Stock("GHI", "GHI", 14, 14, 1.8)
    stock4 = Stock("JKL", "JKL", 16, 16, 2.2)
    stock5 = Stock("MNO", "MNO", 18, 18, 2.4)
    print(stock1.name)

def list_stocks():
    #stock1
    numstocks = 5
    for i in range(numstocks):
        print("stock" + str(i))

def main():
    create_market()
    list_stocks()

main()


    # stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
    # price = []
    # starting_price = {}
    # print(len(stocks))
    # for x in range(len(stocks)):
    #     price.append(rnd.randint(10, 20))
    #     starting_price = price
    #     print("Price List", price)
    #     print("Starting Price List:", starting_price)
    #     #full_prices.append(dict(zip(price, starting_price)))
    # #print(price)
    # full_prices = dict(zip(price, starting_price))
    # #print(full_prices)
    # print(stocks)
    # print(full_prices)
    # #prices = []
    # #starting_price = []
    #
    # # for x in range(len(stocks)):
    # #     prices.append(rnd.randint(10,20))
    # #     #starting_price = prices
    # market = dict(zip(stocks, full_prices))
    #
    # #market = dict(zip(stocks, price, starting_price))

