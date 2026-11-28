import sys
from collections import defaultdict
input = sys.stdin.readline

def sieve(n):
    isPrime = [1 for _ in range(n+1)]
    isPrime[0] = False
    isPrime[1] = False
    m = int(n**0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i ** 2, n+1, i):
                isPrime[j] = False
    primes = []
    for i in range(n+1):
        if isPrime[i]:
            primes.append(i)
    return primes

n, r, mod = map(int, input().split())
a, b, c = n, n-r, r
primes = sieve(n+1)
factor_a, factor_b, factor_c = (defaultdict(int) for _ in range(3))
for i in primes:
    mul = i
    while a >= mul:
        factor_a[i] += a // mul
        mul *= i
for i in primes:
    mul = i
    while b >= mul:
        factor_b[i] += b // mul
        mul *= i
for i in primes:
    mul = i
    while c >= mul:
        factor_c[i] += c // mul
        mul *= i
ret = 1
for i in primes:
    ret *= pow(i, factor_a[i]-factor_b[i]-factor_c[i], mod)
    ret %= mod
print(ret)