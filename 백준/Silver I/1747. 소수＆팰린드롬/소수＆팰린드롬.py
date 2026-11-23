def eratosthenes(n):
    e = [True for _ in range(n+1)]
    e[0], e[1] = False, False
    primes = list()
    for i in range(2, n+1):
        if e[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                e[j] = False
    return primes

primes = eratosthenes(1003001)

n = int(input())
while True:
    if str(n) == str(n)[::-1]:
        if n in primes:
            print(n)
            break
    n += 1