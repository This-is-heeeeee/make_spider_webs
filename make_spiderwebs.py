import ccxt

api_key = ""
sec_key = ""

with open("key.txt") as keys:
    for line in keys:
        key, val = line.split('=')
        if key == "api_key":
            api_key = val.rstrip()
        else:
            sec_key = val.rstrip()

binance = ccxt.binance(config={
    'apiKey' : api_key,
    'secret' : sec_key,
    'enableRateLimit' : True,
    'options' : {
        'defaultType' : 'future'
    }
})

"""
def get_current_price(symbol):
    cp = binance.fetch_ticker(symbol)
    return cp

def get_amount_of_order(symbol) :
    cp = get_current_price(symbol)
    balance = binance.fetch_balance(params={"type" : "future"})
    amount = balance['USDT']
"""

def limit_buy(symbol, amount, price) :
    binance.create_limit_buy_order(symbol, amount, price)

def limit_sell(symbol, amount, price) :
    binance.create_limit_sell_order(symbol, amount, price)

def main() :

    symbol = input("코인 : ")    #ex"BTC"
    price = float(input("가격 : "))
    gap = float(input("간격 : "))
    amount = float(input("갯수 : "))
    split = int(input("분할 수 : "))
    order = input("buy or sell : ")

    symbol = symbol.upper()
    symbol = symbol + "/USDT"

    if order == "buy" :
        for i in range(split) :
            limit_buy(symbol, amount, price)
            price -= gap

    elif order == "sell" :
        for i in range(split) :
            limit_sell(symbol, amount, price)
            price += gap



if __name__ == "__main__" :
    main()