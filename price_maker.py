import random as rnd

stockList = []

class Stock:
    def __init__(self, name, ticker, starting_price, current_price):
        self.name = name
        self.ticker = ticker
        self.starting_price = starting_price
        self.current_price = current_price
        #self.volatility = volatility

def fill_Market():
    global stockList
    nameList = ("American Broadcasting Corp", "Diversified Energy Force", "Global Health Inc", "Jasmine Kiloton LLC", "Minnesota Natural Order")
    tickerList = ("ABC", "DEF", "GHI", "JKL", "MNO")

    for i in range(len(nameList)):
        stockName = nameList[i]
        stockTicker = tickerList[i]
        price = (rnd.randint(10 ,20))
        stockList.append(Stock(stockName, stockTicker, price, price))

def check_Market():
    print()
    for stock in stockList:
        print("  ", stock.name, stock.ticker, stock.starting_price, stock.current_price)

def main():
    fill_Market()
    check_Market()

main()