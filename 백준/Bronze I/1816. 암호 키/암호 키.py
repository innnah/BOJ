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

primes = sieve(1000000)
n = int(input())
for _ in range(n):
    i = int(input())
    for j in range(1000001):
        if primes[j]:
            if i % j == 0:
                print("NO")
                break
    else:
        print("YES")