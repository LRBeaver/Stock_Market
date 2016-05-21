import random as rnd

def create_market():
    global market
    stocks = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'XYZ']
    price = []
    starting_price = {}
    print(len(stocks))
    for x in range(len(stocks)):
        price.append(rnd.randint(10, 20))
        starting_price = price
        print("Price List", price)
        print("Starting Price List:", starting_price)
        #full_prices.append(dict(zip(price, starting_price)))
    #print(price)
    full_prices = dict(zip(price, starting_price))
    #print(full_prices)
    print(stocks)
    print(full_prices)
    #prices = []
    #starting_price = []

    # for x in range(len(stocks)):
    #     prices.append(rnd.randint(10,20))
    #     #starting_price = prices
    market = dict(zip(stocks, full_prices))

    #market = dict(zip(stocks, price, starting_price))


def main():
    create_market()
    print(len(market))
    print(market)
    print(market["ABC"])
    #ticker = input("what ticker shall we work with? ")
    #print('The price of ' + ticker + ' is: $', market[ticker])
    #print(ticker[1])

main()
