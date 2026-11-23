import sys

input = sys.stdin.readline

def sieve(n):
    isPrime = [True] * (n+1)
    isPrime[0] = False
    isPrime[1] = False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i ** 2, n+1, i):
                isPrime[j] = False

    primes = []
    for i in range(2, n+1):
        if isPrime[i]:
            primes.append(i)

    return primes

l = sieve(1120)
dp = [[0 for _ in range(15)] for _ in range(1121)]
dp[0][0] = 1
for i in range(len(l)):
    for j in range(1120, l[i]-1, -1):
        for k in range(1, 15):
            if j < l[i]: break
            dp[j][k] += dp[j-l[i]][k-1]
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(dp[n][k])