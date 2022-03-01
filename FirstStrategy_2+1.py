market_price = float(input("Market Price: "))
balance = float(input("Balance: "))

def short(mp, bl):
    print("First short order")
    stop_price = round(mp * 1.02, 1)
    tp = mp
    sl = round(mp * 1.029, 1)
    size = bl / stop_price
    print(f"Stop Price: {stop_price}")
    print(f"Size: {size:.4f}")
    print(f"Take Profit: {tp}")
    print(f"Stop Loss: {sl}")

    print("\nSecond short order")
    stop_price = round(mp * 1.049, 1)
    tp = round(mp * 1.029, 1)
    sl = round(mp * 1.058, 1)
    size = bl / stop_price
    print(f"Stop Price: {stop_price}")
    print(f"Size: {size:.4f}")
    print(f"Take Profit: {tp}")
    print(f"Stop Loss: {sl}\n\n")

def long(mp, bl):
    print("First long order")
    stop_price = round(mp * 0.98, 1)
    tp = mp
    sl = round(mp * 0.971, 1)
    size = bl / stop_price
    print(f"Stop Price: {stop_price}")
    print(f"Size: {size:.4f}")
    print(f"Take Profit: {tp}")
    print(f"Stop Loss: {sl}")

    print("\nSecond long order")
    stop_price = round(mp * 0.951, 1)
    tp = round(mp * 0.971, 1)
    sl = round(mp * 0.942, 1)
    size = bl / stop_price
    print(f"Stop Price: {stop_price}")
    print(f"Size: {size:.4f}")
    print(f"Take Profit: {tp}")
    print(f"Stop Loss: {sl}")

short(market_price, balance)
long(market_price, balance)