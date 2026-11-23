import math

def sieve(n):
    if n % 2 == 0:
        flags = [True, True, False, False] + [True, False] * ((n - 2) // 2) + [True]
    else:
        flags = [True, True, False, False] + [True, False] * ((n - 2) // 2)
    sqrtn = math.floor(math.sqrt(n))
    primes = []
    
    for i in range(3, sqrtn + 1, 2):
        if flags[i] == True:
            continue

        for x in range(i * i, n + 1, i * 2):
            flags[x] = True

    for y in range(len(flags)):
        if not flags[y]:
            primes.append(y)

    return primes

def factorize2(n, mpf):
    factors = []
    deleted = 0

    if n in mpf:
        return [[n, 1]]

    for x in range(len(mpf)):
        if n < mpf[x]:
            break

        factors.append([mpf[x], 0])

        while n % mpf[x] == 0:
            factors[x - deleted][1] += 1
            n //= mpf[x]

        if factors[x - deleted][1] == 0:
            del factors[x - deleted]
            deleted += 1

    if n > 1:
        factors.append([n, 1])

    return factors

t = int(input())
for _ in range(t):
    n = int(input())
    primes = sieve(math.isqrt(n) + 1)
    factors = factorize2(n, primes)

    for x in factors:
        a, b = map(int, x)
        print(a, b)  