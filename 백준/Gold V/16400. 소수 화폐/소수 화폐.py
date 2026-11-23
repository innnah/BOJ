mod = 123456789
def sieve(n):
    isPrime[0] = False
    isPrime[1] = False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i ** 2, n+1, i):
                isPrime[j] = False

def solve(n, coins):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], n+1):
            dp[j] += dp[j-coins[i]]
            dp[j] %= mod
    return dp[n]

n = int(input())
isPrime = [True] * (n+1)
primes = []
sieve(n)
for i in range(n+1):
    if isPrime[i]:
        primes.append(i)
print(solve(n, primes)%mod)