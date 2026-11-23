import sys

input = sys.stdin.readline

def solve(n, coins):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], n+1):
            dp[j] += dp[j-coins[i]]
    return dp[n]

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    toMake = int(input())
    print(solve(toMake, coins))