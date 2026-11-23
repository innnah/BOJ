def getlcd(n):
    lcd = []
    for i in range(n, 0, -1):
        if n % i == 0:
            lcd.append(n // i)
            lcd.append(i)

    return lcd

def getEqualLcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return getlcd(i)

a, b = map(int, input().split())

lcd = list(set([1] + getEqualLcd(a, b)))
lcd.sort()

for x in lcd:
    print(x, a // x, b // x)