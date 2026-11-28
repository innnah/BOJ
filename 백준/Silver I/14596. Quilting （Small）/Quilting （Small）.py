import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
dp = [[10**20 for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[0][i] = (a[0][i] - b[0][i]) ** 2
for i in range(1, n):
    for j in range(m):
        if j != 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j])
        if j != m-1:
            dp[i][j] = min(dp[i-1][j+1], dp[i][j])
        dp[i][j] = min(dp[i-1][j], dp[i][j]) + (a[i][j] - b[i][j]) ** 2
print(min(dp[n-1]))