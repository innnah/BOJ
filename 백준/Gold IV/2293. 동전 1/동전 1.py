import sys

input = sys.stdin.readline

def solve(n, coins):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    return dp[n]

n, k = map(int, input().split())
l = list(set([int(input()) for _ in range(n)]))
l.sort()
ret = solve(k, l)
print(ret)