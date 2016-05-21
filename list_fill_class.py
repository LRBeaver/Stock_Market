import random as rnd

class Stock:
    def __init__(self, name, ticker, starting_price, current_price):
        self.name = name
        self.ticker = ticker
        self.starting_price = starting_price
        self.current_price = current_price
        #self.volatility = volatility

    def list_stocks(self):
        numStocks = 5
        print("--------------------")
        #for i in range(numStocks):
        print ("Stock name is " + self.name + " and ticker is " + self.ticker + " and the price is " + str(self.starting_price))

    # def __iter__(self, name, ticker, starting_price, current_price, volatility):
    # stock = Stock(self, name, ticker, starting_price, current_price, volatility)
    # for attr, value in stock.__dict__.items():
    #     print(attr, value)

class Market:
    def __init__(self):
        self.contents =[Stock(*content) for content in Stock]

#numStocks = 5

stock1 = Stock("American Broadcasting Corp", "ABC", 10, 10)
stock2 = Stock("Diversified Energy Force", "DEF", 12, 12)
stock3 = Stock("Global Health Inc", "GHI", 14, 14)
stock4 = Stock("Jasmine Kiloton LLC", "JKL", 16, 16)
stock5 = Stock("Minnesota Natural Order", "MNO", 18, 18)

stock1.volatility = 1  # Add an 'age' attribute.

#market = {stock1, stock2, stock3, stock4, stock5}


stock1.list_stocks()
#print(hasattr(stock1, 'ticker'))
print(getattr(stock1, 'ticker'))
print(hasattr(stock1, 'volatility'))
print(getattr(stock1, 'volatility'))
stock2.list_stocks()
#print(hasattr(stock2, 'ticker'))
print(getattr(stock2, 'ticker'))
print(hasattr(stock2, 'volatility'))
if (hasattr(stock2, 'volatility')):
    print(getattr(stock2, 'volatility'))
else:
    pass
stock3.list_stocks()
#print(hasattr(stock3, 'ticker'))
print(getattr(stock3, 'ticker'))
stock4.list_stocks()
#print(hasattr(stock4, 'ticker'))
print(getattr(stock4, 'ticker'))
stock5.list_stocks()
#print(hasattr(stock5, 'ticker'))
print(getattr(stock5, 'ticker'))
print(Market)





