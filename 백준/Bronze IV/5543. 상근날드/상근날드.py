burgerPrices = [int(input()) for _ in range(3)]
drinkPrices = [int(input()) for _ in range(2)]

print(min(burgerPrices) + min(drinkPrices) - 50)