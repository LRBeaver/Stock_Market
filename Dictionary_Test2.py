#dict["Apple"]["American"]
import random as rnd
portfolio = {}

def make_market():
    global market
    stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
    prices = []

    for x in range(len(stocks)):
        prices.append(rnd.randint(10, 20))

    market = dict(zip(stocks, prices))


#portfolio.update({choice: {cost : shares}})
def buy_stock():
    global portfolio
    print(market)
    choice = input('What stock do you want to buy?: ')
    print('The price of ' + choice + ' is: $', market[choice])
    print('\n' + "----------------------")
    shares = input('How many shares do you want?: ')
    cost = int(shares) * int(market[choice])
    portfolio.update({choice: {cost: shares}})
    print(portfolio)
    print("You have " + portfolio['ABC'][cost] + ' shares')


def main():
    make_market()
    buy_stock()

main()