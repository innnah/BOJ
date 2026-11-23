n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
s = sum(costs)
mincost = 987654321
dp = [[0] * (s+1) for _ in range(n+1)]
dp[1][costs[0]] = memories[0]
if dp[1][costs[0]] >= m: mincost = costs[0]
for i in range(2, n+1):
    for j in range(s+1):
        if dp[i-1][j] != 0 or j == 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            dp[i][j+costs[i-1]] = max(dp[i][j+costs[i-1]], dp[i-1][j] + memories[i-1])
            if dp[i][j] >= m: mincost = min(mincost, j)
            if dp[i][j+costs[i-1]] >= m: mincost = min(mincost, j+costs[i-1])
print(mincost)