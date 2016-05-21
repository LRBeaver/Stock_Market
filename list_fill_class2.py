import random as rnd
stockList = []

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

def fillMarket():
    global stockList

    stockList.append(Stock("American Broadcasting Corp", "ABC", 10, 10))
    stockList.append(Stock("Diversified Energy Force", "DEF", 12, 12))
    stockList.append(Stock("Global Health Inc", "GHI", 14, 14))
    stockList.append(Stock("Jasmine Kiloton LLC", "JKL", 16, 16))
    stockList.append(Stock("Minnesota Natural Order", "MNO", 18, 18))

def check_market():
    print("-----------------")
    print("Showing one stock item")
    print(stockList[0].ticker)
    print()
    print ("Sort the stockList in place by ticker ...")
    import operator
    stockList.sort(key=operator.attrgetter('ticker'))
    print("-----------------")
    print("Iterate through the list")
    print()
    for stock in stockList:
        print("  ", stock.name, stock.ticker, stock.starting_price)
    print()
    print("-----------------")
    print("Show the starting_prince(s) of a specific ticker:")
    look = 'ABC'
    for stock in stockList  :
        if look in stock.ticker:
            # title() capitalizes the job's first letter
            print ("%s %s: \"%s\"" % (stock.ticker.title(), stock.name, stock.starting_price))
    print()
    print("-----------------")
    print ("What the heck is the ticker of Minnesota Natural Order?")
    look = "Minnesota Natural Order"
    for stock in stockList:
        if look in stock.name:
            print ("%s: \"%s\"" % (stock.name, stock.ticker))


def main():
    fillMarket()
    check_market()



main()