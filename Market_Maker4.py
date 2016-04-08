__author__ = 'lyndsay.beaver'
#import sqlite3 as sq1
import random as rnd

#"{:,}".format(value)

starting = 10000
balance = starting
portfolio = {}
goto_menu = True

def create_market():
    global market
    stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
    prices = []

    for x in range(len(stocks)):
        prices.append(rnd.randint(10,20))

    market = dict(zip(stocks, prices))
    #print(len(market))
    #return market
#
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

def check_market():
    print('\n'+"----------------------")
    print('\n'+"You chose to check the market")
    print(market)
    #else:
        #create_market()


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
    print(market)
    choice = input('What stock do you want to buy?: ')
    print('The price of ' + choice + ' is: $', market[choice])
    print('\n'+"----------------------")
    shares = input('How many shares do you want?: ')
    cost = int(shares) * int(market[choice])
    portfolio.update({choice: {market[choice] : shares}})
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
            #print('The price of ' + ticker + ' is: $', market[ticker])
            print(portfolio)
            ("You have :" + portfolio(sold_ticker(shares)))
            print("You have ${:,}".format(portfolio[sold_ticker]) + " worth of shares")
            #shares_to_sell=input("How many shares would you like to sell?: ")
            #if shares_to_sell <= owned_shares:
                #print("Selling x shares:")

def menu():
    #print(portfolio)
    #print()
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
        check_market()

    elif action == '2':
        #if 'portfolio' in locals():
        check_portfolio()
             #print("You have ${:,}".format(balance))
        #else:
            #print('\n'+"----------------------")
            #print("You own no stocks")
            #print("You have ${:,}".format(balance))

    elif action == '3':
        buy_stocks()

    elif action == '4':
        #if 'portfolio' in locals():
        sell_stocks()
        #else:
            #print('\n'+"----------------------")
            #print("Your portfolio is empty")
            #print("You have ${:,}".format(balance))

    else:
        print('\n'+"----------------------")
        print("Starting new day...")
        quit()

def main():
    print("Main fired")
    create_market()
    #insert(passed_market)
    #owned_portfolio = {}
    #starting_balance=0
    #starting = 10000
    #balance = starting
    #returned_portfolio = ()
    while goto_menu:
        menu()

main()