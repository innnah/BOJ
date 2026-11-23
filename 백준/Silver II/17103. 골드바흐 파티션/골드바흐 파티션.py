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

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n//2+1):
        if sieve[i] and sieve[n-i]:
            cnt += 1
    print(cnt)