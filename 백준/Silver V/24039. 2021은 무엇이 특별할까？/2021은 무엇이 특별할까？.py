def sieve(n:int) -> list:
    isPrime = [True] * (n+1)
    isPrime[0] = False
    isPrime[1] = False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i ** 2, n+1, i):
                isPrime[j] = False

    primes = []
    for i in range(n+1):
        if isPrime[i]:
            primes.append(i)

    return primes

l = sieve(200)
n = int(input())
i = 0
while l[i] * l[i+1] <= n: i += 1
print(l[i] * l[i+1])