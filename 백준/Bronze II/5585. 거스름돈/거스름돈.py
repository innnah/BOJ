money = 1000 - int(input())
cnt = 0
moneyType = [500, 100, 50, 10, 5, 1]

for x in moneyType:
    cnt += money // x
    money %= x

    if money == 0:
        break

print(cnt)