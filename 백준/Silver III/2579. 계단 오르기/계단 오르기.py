import sys

input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
if n < 3:
    print(sum(l))
    sys.exit(0)
dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[1][1] = l[0]
dp[2][1] = l[1]
dp[2][2] = sum(l[:2])
for i in range(3, n+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + l[i-1]
    dp[i][2] = dp[i-1][1] + l[i-1]
print(max(dp[n][1], dp[n][2]))