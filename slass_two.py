import random as rnd

class Stock:
    def __init__(self, name, ticker, starting_price, current_price, volatility):
        self.name = name
        self.ticker = ticker
        self.starting_price = starting_price
        self.current_price = current_price
        self.volatility = volatility

    def list_stocks(self):
        numStocks = 5
        print("--------------------")
        #for i in range(numStocks):
        print ("Stock name is " + self.name + " and ticker is " + self.ticker + " and the price is " + str(self.starting_price))

    # def __iter__(self, name, ticker, starting_price, current_price, volatility):
    # stock = Stock(self, name, ticker, starting_price, current_price, volatility)
    # for attr, value in stock.__dict__.items():
    #     print(attr, value)


global market
#numStocks = 5

stock1 = Stock("American Broadcasting Corp", "ABC", 10, 10, 1)
stock2 = Stock("Diversified Energy Force", "DEF", 12, 12, 1.2)
stock3 = Stock("Global Health Inc", "GHI", 14, 14, 1.8)
stock4 = Stock("Jasmine Kiloton LLC", "JKL", 16, 16, 2.2)
stock5 = Stock("Minnesota Natural Order", "MNO", 18, 18, 2.4)

#market = {stock1, stock2, stock3, stock4, stock5}


stock1.list_stocks()
print(hasattr(stock1, 'ticker'))    # Returns true if 'age' attribute exists
print(getattr(stock1, 'ticker'))
stock2.list_stocks()
stock3.list_stocks()
stock4.list_stocks()
stock5.list_stocks()





