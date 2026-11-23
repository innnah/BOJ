dp = [[-1 for _ in range(101)] for _ in range(101)]
def bino(n, r):
    if r == 0 or n == r: return 1
    if dp[n][r] != -1: return dp[n][r]
    dp[n][r] = bino(n-1, r) + bino(n-1, r-1)
    return dp[n][r]

n, r = map(int, input().split())
print(bino(n, r))