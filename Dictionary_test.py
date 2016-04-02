import random as rnd

def create_market():
    global market
    stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
    prices = []

    for x in range(len(stocks)):
        prices.append(rnd.randint(10,20))

    market = dict(zip(stocks, prices))


def main():
    create_market()
    print(len(market))
    print(market)
    ticker = input("what ticker shall we work with? ")
    print('The price of ' + ticker + ' is: $', market[ticker])
    #print(ticker[1])

main()
