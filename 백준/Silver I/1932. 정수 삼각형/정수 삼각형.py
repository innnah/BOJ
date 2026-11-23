import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * n for _ in range(n)]
l = [list(map(int, input().split())) for _ in range(n)]
dp[0][0] = l[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j != 0: 
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + l[i][j])
        if j != i:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + l[i][j])
print(max(dp[-1]))