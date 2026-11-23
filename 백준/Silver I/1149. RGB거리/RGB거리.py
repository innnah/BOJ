import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(4)] for _ in range(n+1)]
dp[1] = [0] + l[0].copy()
for i in range(2, n+1):
    dp[i][1] = min(dp[i-1][2], dp[i-1][3]) + l[i-1][0]
    dp[i][2] = min(dp[i-1][1], dp[i-1][3]) + l[i-1][1]
    dp[i][3] = min(dp[i-1][1], dp[i-1][2]) + l[i-1][2]
print(min(dp[n][1], dp[n][2], dp[n][3]))