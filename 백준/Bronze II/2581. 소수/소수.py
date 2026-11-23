import math, sys

def isPrime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False

    if n < 4:
        return True

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

m = int(input())
n = int(input())
primes = []

for x in range(m, n+1):
    if isPrime(x):
        primes.append(x)
        
if len(primes) == 0:
    print(-1)
    sys.exit(0)
        
print(sum(primes))
print(min(primes))