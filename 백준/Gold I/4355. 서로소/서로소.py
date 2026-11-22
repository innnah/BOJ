import sys
input = sys.stdin.readline

primes = []
isPrime = [1 for _ in range(32001)]
isPrime[0] = isPrime[1] = 0
for i in range(2, 32001):
    if isPrime[i]:
        primes.append(i)
        for j in range(i*i, 32001, i):
            isPrime[j] = 0

while 1:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(0)
        continue
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
    if n != 1:
        factors.append(n)
    ans = factors[0]-1
    for i in range(1, len(factors)):
        if factors[i] != factors[i-1]:
            ans *= factors[i]-1
        else:
            ans *= factors[i]
    print(ans)