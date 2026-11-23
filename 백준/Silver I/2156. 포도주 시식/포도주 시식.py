import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][1] = l[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = l[i] + dp[i-1][0]
    dp[i][2] = l[i] + dp[i-1][1]
print(max(dp[-1]))