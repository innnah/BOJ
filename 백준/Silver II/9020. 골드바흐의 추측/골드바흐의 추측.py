import sys

input = sys.stdin.readline

sieve = [True] * 10001
sieve[0] = False
sieve[1] = False

m = int(10000 ** 0.5)
for i in range(2, m+1):
    if sieve[i]:
        for j in range(i ** 2, 10001, i):
            sieve[j] = False

j = int(input())
for _ in range(j):
    n = int(input())
    for i in range(n//2, n+1):
        if sieve[i] and sieve[n-i]:
            print(n-i, i)
            break