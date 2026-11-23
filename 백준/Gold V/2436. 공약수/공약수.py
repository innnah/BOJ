import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return (a*b)//gcd(a,b)

a, b = map(int, input().split())
multi = a*b
num = math.floor(math.sqrt(multi))

while True:
    if multi % num == 0:
        c, d = num, multi // num
        if gcd(c, d) == a and lcm(c, d) == b:
            print(c, d)
            break
    num -= 1