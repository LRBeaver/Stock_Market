import random as rnd

starting = 10000
balance = starting
portfolio = {}
goto_menu = True
stockList = []

class Stock:
    def __init__(self, name, ticker, starting_price, current_price, volatility):
        self.name = name
        self.ticker = ticker
        self.starting_price = starting_price
        self.current_price = current_price
        self.volatility = volatility

def create_Market():
    global stockList
    nameList = ("American Broadcasting Corp", "Diversified Energy Force", "Global Health Inc",
                "Jasmine Kiloton LLC", "Minnesota Natural Order")
    tickerList = ("ABC", "DEF", "GHI", "JKL", "MNO")

    for i in range(len(nameList)):
        stockName = nameList[i]
        stockTicker = tickerList[i]
        price = (rnd.randint(10, 20))
        volatility = (rnd.randint(1, 3))
        stockList.append(Stock(stockName, stockTicker, price, price, volatility))

class Portfolio:
    def __init__(self, ticker, purchase_price, num_shares):
        self.ticker = ticker
        self.purchase_price = purchase_price
        self.num_shares = num_shares

def buy_stocks():
    global Portfolio
    global balance
    global portfolio
    print('\n'+"----------------------")
    print("You chose to buy stocks")
    print("You have ${:,}".format(balance))
    #print(stockList)
    for stock in stockList:
        print("  ", stock.ticker, stock.name, stock.current_price)
    choice = input('What stock do you want to buy?: ')
    for stock in stockList:
        if choice in stock.ticker:
            print("Inside Choice")
            print("The price of %s %s is: \"%s\"" % (stock.ticker, stock.name, stock.current_price))
            print('\n' + "----------------------")
            shares = input('How many shares do you want?: ')
            cost = int(shares) * int(stock.current_price)
            print(cost)
            portfolio1 = Portfolio(stock.ticker, stock.current_price, shares)
            portfolio = {portfolio1.ticker, portfolio1.purchase_price, portfolio1.num_shares}
            print(portfolio1.ticker, portfolio1.purchase_price, portfolio1.num_shares)
            print(portfolio)
            #cost = portfolio1.purchase_price * portfolio1.num_shares
            print("Cost of this transaction was: ", cost)
def main():
    create_Market()
    buy_stocks()


main()