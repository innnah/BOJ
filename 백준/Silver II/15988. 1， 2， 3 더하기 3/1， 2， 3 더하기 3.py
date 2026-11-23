import sys

input = sys.stdin.readline

mod = 1000000009
def solve(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] += dp[i-1] % mod + dp[i-2] % mod + dp[i-3] % mod

    return dp

l = solve(1000000)
for _ in range(int(input())):
    print(l[int(input())] % 1000000009)