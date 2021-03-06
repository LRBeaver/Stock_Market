__author__ = 'lyndsay.beaver'
import sqlite3 as sq1
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
    if 'balance' in locals():
        #current_balance=balance
        if portfolio == {}:
            print("You own no stocks")
            print("You have ${:,}".format(balance))
        else:
            print('Portfolio: ', owned_portfolio)
            print('Cash: ${:,}'.format(current_balance))
    else:
        if owned_portfolio == {}:
            print("You own no stocks")
            print("You have ${:,}".format(balance))
        else:
            print('Portfolio: ', owned_portfolio)

            print('Cash: ${:,}'.format(current_balance))

def buy_stocks():
    global portfolio
    global balance
    #global market
    #print(balance)
    #cash_available = 10000
    print('\n'+"----------------------")
    print("You chose to buy stocks")
    print("You have ${:,}".format(balance))
    print(market)
    choice = input('What stock do you want to buy?: ')
    print('The price of ' + choice + ' is: $', market[choice])
    print('\n'+"----------------------")
    shares = input('How many shares do you want?: ')
    cost = int(shares) * int(market[choice])
    portfolio={choice:cost}
    #portfolio = owned_portfolio
    print("This transaction will cost: ${:,}".format(cost))
    balance = balance-cost
    print("You now have this much cash left: ${:,}".format(balance))
    print(portfolio)
    print(balance)
    #return owned_portfolio, returned_balance

def sell_stocks():
    global portfolio
    global balance
    print('\n'+"----------------------")
    print("You chose to sell stocks")
    sold_ticker=input("What stock would you like to sell?: ")
    if sold_ticker in portfolio:
        print('\n'+"----------------------")
        shares_to_sell=input("How many shares would you like to sell?: ")
        if shares_to_sell <= owned_shares:
            print("Selling x shares:")

def menu():
    print(portfolio)
    print()
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
        if 'market' in locals():
            print("Used existing")
            check_market()
        else:
            print("Had to make a new one")
            market=create_market()
            check_market()

    elif action == '2':
        if 'portfolio' in locals():
            check_portfolio()
             #print("You have ${:,}".format(balance))
        else:
            print('\n'+"----------------------")
            print("You own no stocks")
            print("You have ${:,}".format(balance))

    elif action == '3':
        if 'market' in locals():
            print("Used existing")
            owned_portfolio=(buy_stocks())
        else:
            print("Had to make a new one")
            market=create_market()
            owned_portfolio=(buy_stocks())

    elif action == '4':
        if 'portfolio' in locals():
            sell_stocks()
        else:
            print('\n'+"----------------------")
            print("Your portfolio is empty")
            print("You have ${:,}".format(balance))

    else:
        print('\n'+"----------------------")
        print("Starting new day...")
        quit()

def main():
    create_market()
    #insert(passed_market)
    #owned_portfolio = {}
    #starting_balance=0
    #starting = 10000
    #balance = starting
    #returned_portfolio = ()
    print("Main fired")
    while goto_menu:
        menu()

main()