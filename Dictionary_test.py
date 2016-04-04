import random as rnd

def create_market():
    global market
    stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
    for x in range(len(stocks)):
        price = (rnd.randint(10, 20))
        starting_price = price

    full_prices = dict(zip(price, starting_price)
    print(full_prices)

    #prices = []
    #starting_price = []

    # for x in range(len(stocks)):
    #     prices.append(rnd.randint(10,20))
    #     #starting_price = prices
    #market = dict(zip(stocks, full_prices))

    #market = dict(zip(stocks, price, starting_price))


def main():
    create_market()
    print(len(market))
    print(market)
    ticker = input("what ticker shall we work with? ")
    print('The price of ' + ticker + ' is: $', market[ticker])
    #print(ticker[1])

main()
