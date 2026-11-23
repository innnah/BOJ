import sys

input = sys.stdin.readline

sieve = [True] * 1000001
sieve[0] = False
sieve[1] = False

m = int(1000000 ** 0.5)
for i in range(2, m+1):
    if sieve[i]:
        for j in range(i ** 2, 1000001, i):
            sieve[j] = False

while True:
    n = int(input())
    if n == 0: break

    for i in range(n):
        if sieve[i] and sieve[n-i]:
            print(f"{n} = {i} + {n-i}")
            break