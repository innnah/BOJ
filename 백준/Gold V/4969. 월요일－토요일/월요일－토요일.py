isPrime = [1 for _ in range(300001)]
isPrime[0] = False
isPrime[1] = False
m = int(300000 ** 0.5)
for i in range(2, m+1):
    if i % 7 in (1, 6):
        if isPrime[i]:
            for j in range(i ** 2, 300000, i):
                isPrime[j] = False

primes = []
for i in range(1, 300001):
    if i % 7 in (1, 6):
        if isPrime[i]:
            primes.append(i)
while 1:
    n = int(input())
    if n == 1: break
    print(f"{n}: ", end = '')
    for p in primes:
        if n % p == 0:
            print(p, end = ' ')
    print()