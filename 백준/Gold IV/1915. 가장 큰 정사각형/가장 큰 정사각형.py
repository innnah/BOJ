import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
ret = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i-1][j-1] != 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        ret = max(ret, dp[i][j])
print(ret**2)