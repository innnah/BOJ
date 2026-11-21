import sys, random
from collections import defaultdict

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x*x) % p
    return res
 
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
 
def miller_rabin(n, a):
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d = d//2

    x = power(a, d, n)
    if x == 1 or x == n-1:
        return True

    for _ in range(r-1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False
 
def is_prime(n):
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for a in alist:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True
 
 
def pollardRho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollardRho(n)
    if is_prime(d):
        return d
    else:
        return pollardRho(d)

n = int(input())
n2 = n
n3 = n
factors = defaultdict(int)
while n > 1:
    divisor = pollardRho(n)
    factors[divisor] += 1
    n //= divisor
while n2 % 4 == 0:
    n2 //= 4
if n2 % 8 == 7:
    print(4)
    sys.exit(0)
keys = factors.keys()
for i in keys:
    if i % 4 == 3:
        if factors[i] % 2 == 1:
            print(3)
            sys.exit(0)
if int(n3 ** 0.5) ** 2 == n3:
    print(1)
else:
    print(2)