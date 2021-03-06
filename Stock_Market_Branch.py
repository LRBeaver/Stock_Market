__author__ = 'lyndsay.beaver'
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

# class Portfolio:
#     def __init__(self, ticker, purchase_price, num_shares):
#         self.ticker = ticker
#         self.purchase_price = purchase_price
#         self.num_shares = num_shares


# def insert(market):
#     #print("Number of stocks: ", len(market))
#     database1 = sq1.connect('stocks' + str(rnd.randint(1,200)) + '.db')
#     db1_cursor = database1.cursor()
#
#     db1_cursor.execute('CREATE TABLE stocks(ticker TEXT, prices TEXT, current TEXT)')
#
#     list = market.keys()
#     for i in list:
#         tmp1 = i
#         tmp2 = market[i]
#         tmp3 = 0
#
#         db1_cursor.execute('INSERT INTO stocks VALUES(?,?, ?)', (tmp1, tmp2, tmp3))
#
#     database1.commit()
#     db1_cursor.close()
#     database1.close()

def check_Market():
    print('\n'+"----------------------")
    print('\n'+"You chose to check the market")
    print()
    for stock in stockList:
        print("  ", stock.name, stock.ticker, stock.starting_price, stock.current_price, stock.volatility)
    for stock in stockList:
        print()
        look = 'ABC'
        if look in stock.ticker:
            print("%s %s: \"%s\"" % (stock.ticker, stock.name, stock.starting_price))


def check_portfolio():
    print('\n'+"----------------------")
    print("You chose to check your portfolio")
    print('\n' + "******************")
    if portfolio == {}:
        print("You own no stocks")
        print("You have ${:,}".format(balance))
    else:
        print('Portfolio: ', portfolio)
        print('Cash: ${:,}'.format(balance))

def buy_stocks():
    global portfolio
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
            if choice in portfolio:
                print("Update")
                portfolio.update({choice: {cost: int(shares)}})
                #print(portfolio.ticker, cost, shares)
            else:
                print("New")
                portfolio.update({choice: {cost: int(shares)}})
    print("This transaction will cost: ${:,}".format(cost))
    balance = balance-cost
    print("You now have this much cash left: ${:,}".format(balance))
    print(portfolio)
    print(balance)

def sell_stocks():
    global portfolio
    global balance
    if portfolio == {}:
        print('\n' + "----------------------")
        print("Your portfolio is empty")
        print("You have ${:,}".format(balance))
    else:
        print('\n'+"----------------------")
        print("You chose to sell stocks")
        print(portfolio)
        sold_ticker=input("What stock would you like to sell?: ")
        if sold_ticker in portfolio:
            print('\n'+"----------------------")
            print(portfolio)
            ("You have :" + portfolio(sold_ticker(shares)))
            print("You have ${:,}".format(portfolio[sold_ticker]) + " worth of shares")

def menu():
    print('\n'+"----------------------")
    print(""" Market game - stocks
        [1] Check the market
        [2] Check your portfolio
        [3] Buy stocks
        [4] Sell stocks
        [5] End the day
        """)

    action = input('What would you like to do?: ')

    if action == '1':
        check_Market()

    elif action == '2':
        check_portfolio()


    elif action == '3':
        buy_stocks()

    elif action == '4':
        sell_stocks()


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