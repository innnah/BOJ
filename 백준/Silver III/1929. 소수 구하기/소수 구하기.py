import math

m, n = map(int, input().split())

def getPrimes(m, n):
    if m != 1:
        flags = [0] * m + [1] * (n - m + 1)
    else:
        flags = [0] * (m + 1) + [1] * (n - m)

    if m == 0:
        flags[0] = flags[1] = 0
    elif m == 1:
        flags[0] = 0

    sqrtn = math.floor(math.sqrt(n))
    for i in range(2, sqrtn + 1):
        if flags[i] == 1 or i < m:
            for j in range(i * i, n + 1, i):
                flags[j] = 0
    
    primes = []
    for i in range(len(flags)):
        if (flags[i] == 1):
            primes.append(i)
    
    return primes

primes = getPrimes(m, n)

for x in primes:
    print(x)