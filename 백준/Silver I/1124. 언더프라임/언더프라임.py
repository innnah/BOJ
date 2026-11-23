def sieve(n):
    isPrime = [True] * (n+1)
    isPrime[0] = False
    isPrime[1] = False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i ** 2, n+1, i):
                isPrime[j] = False

    return isPrime

primes = sieve(100000)

a, b = map(int, input().split())
cache = [1 if primes[i] else 0 for i in range(b+1)]
ret = 0

for i in range(2, b+1):
    for j in range(i, b+1):
        if i * j > b:
            break
        cache[i*j] = cache[i] + cache[j]
for i in range(a, b+1):
    if primes[cache[i]]:
        ret += 1

print(ret)