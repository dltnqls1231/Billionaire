market_price = float(input("Market Price: "))
balance = float(input("Balance: "))

def short(market, balance):
    price = market * 1.02
    stop_price = price - 10
    tp = price * 0.98
    sl = price * 1.009
    size = balance / price
    print(f"Stop Price: {stop_price:.4f}")
    print(f"Price: {price:.4f}")
    print(f"Size: {size:.4f}")
    print(f"Take Profit: {tp:.4f}")
    print(f"Stop Loss: {sl:.4f}\n\n")
    return sl


def long(market, balance):
    price = market * 0.98
    stop_price = price + 10
    tp = price * 1.02
    sl = price * 0.991
    size = balance / price
    print(f"Stop Price: {stop_price:.4f}")
    print(f"Price: {price:.4f}")
    print(f"Size: {size:.4f}")
    print(f"Take Profit: {tp:.4f}")
    print(f"Stop Loss: {sl:.4f}\n\n")
    return sl


loss_balance = balance * 0.99

print("\n\nFirst short order")
next_short = short(market_price, balance)
print("Second short order")
short(next_short, loss_balance)

print("First long order")
next_long = long(market_price, balance)
print("Second long order")
long(next_long, loss_balance)
