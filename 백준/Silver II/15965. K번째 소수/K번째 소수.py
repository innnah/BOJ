import math

def sieve(n):
    if n % 2 == 0:
        flags = [0, 0, 1, 1] + [0, 1] * ((n - 2) // 2) + [0]
    else:
        flags = [0, 0, 1, 1] + [0, 1] * ((n - 2) // 2)
    sqrtn = math.floor(math.sqrt(n))
    primes = []
    
    for i in range(3, sqrtn + 1, 2):
        if flags[i] == 0:
            continue

        for x in range(i * i, n + 1, i * 2):
            flags[x] = 0

    for y in range(len(flags)):
        if flags[y] == 1:
            primes.append(y)

    return primes

n = int(input())
print(sieve(8000000)[n-1])