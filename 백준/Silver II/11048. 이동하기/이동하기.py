n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = l[0][0]
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = l[i][j] + max(dp[i][j+1], dp[i][j], dp[i+1][j])
print(dp[-1][-1])