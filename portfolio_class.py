#import sqlite3 as sq1
import random as rnd

#"{:,}".format(value)

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

def check_Market():
    print('\n'+"----------------------")
    print('\n'+"You chose to check the market")
    print()
    for stock in stockList:
        print("  ", stock.name, stock.ticker, stock.starting_price, stock.current_price, stock.volatility)
    # for stock in stockList:
    #     print()
    #     look = 'ABC'
    #     if look in stock.ticker:
    #         print("%s %s: \"%s\"" % (stock.ticker, stock.name, stock.starting_price))


def buy_stocks():
    global Portfolio
    global balance
    print('\n'+"----------------------")
    print("You chose to buy stocks")
    print("You have ${:,}".format(balance))
    #print(stockList)
    for stock in stockList:
        print("  ", stock.ticker, stock.name, stock.current_price)
    choice = input('What stock do you want to buy?: ')
    for stock in stockList:
        if choice in stock.ticker:
            # title() capitalizes the job's first letter
            print("The price of %s %s is: \"%s\"" % (stock.ticker, stock.name, stock.current_price))
            print('\n'+"----------------------")
            shares = input('How many shares do you want?: ')
            cost = int(shares) * int(stock.current_price)

            if 'portfolio1' in globals():
                print("Exists")
                portfolio1 = Portfolio(stock.ticker, stock.current_price, shares)
                portfolio = portfolio1
                print(portfolio)
            # elif 'portfolio1' in globals():
            #     print("Exists")
            else:
                print("New")
                portfolio1 = Portfolio(stock.ticker, stock.current_price, shares)
                portfolio = portfolio1
                print(portfolio)

    print("This transaction will cost: ${:,}".format(cost))
    balance = balance-cost
    print("You now have this much cash left: ${:,}".format(balance))
    #for p in Portfolio:
    print("  You purchased %s shares of %s stock, for $%s dollars per share" % (portfolio1.num_shares, portfolio1.ticker, portfolio1.purchase_price))
    #print(portfolio)
    print(balance)

def check_portfolio():
    print('\n'+"----------------------")
    print("You chose to check your portfolio")
    print('\n' + "******************")
    if portfolio == {}:
        print("You own no stocks")
        print("You have ${:,}".format(balance))
    else:
        print('Portfolio: ', portfolio1)
        print('Cash: ${:,}'.format(balance))

def menu():
    print('\n'+"----------------------")
    print(""" Market game - stocks
        [1] Check the market
        [2] Check your portfolio
        [3] Buy stocks
        [4] End the day
        """)

    action = input('What would you like to do?: ')

    if action == '1':
        check_Market()

    elif action == '2':
        check_portfolio()


    elif action == '3':
        buy_stocks()


    else:
        print('\n'+"----------------------")
        print("Starting new day...")
        quit()

def main():
    print("Main fired")
    create_Market()
    while goto_menu:
        menu()

main()