prices = [57.8, 46.51, 97, 20.45, 85.27, 29.38, 50, 99.99, 127.33, 72.55, 68.24, 12.40, 17.50]
new_prices = []
for price in prices:
    rubles = int(price)
    kop = round((price - rubles) * 100)
    new_prices.append(f'{rubles} руб {kop:02d} коп')
print(', '.join(new_prices))

id1 = id(prices)
prices.sort()
print(prices)
print(id(prices) == id1)

my_prices = sorted(prices, reverse=True)
print(my_prices)

print(sorted(my_prices[:5]))
