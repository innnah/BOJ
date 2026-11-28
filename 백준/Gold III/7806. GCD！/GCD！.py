import sys

r = 31623
isPrime = [1 for _ in range(r)]
isPrime[0] = isPrime[1] = 0
for i in range(2, r):
    if isPrime[i]:
        for j in range(i*i, 3, i):
            isPrime[j] = 0

primes = []
for i in range(r):
    if isPrime[i]:
        primes.append(i)

lines = sys.stdin.readlines()
for line in lines:
    n, k = map(int, line.split())
    ans = 1
    for i in primes:
        fk = 0
        while k % i == 0:
            k //= i
            fk += 1
        fn = 0
        mul = i
        while n >= mul:
            fn += n // mul
            mul *= i
        ans *= i ** min(fn, fk)
    
    if n >= k:
        ans *= k
    print(ans)