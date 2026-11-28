import sys
input = sys.stdin.readline

n, ri, rg = map(int, input().split())
probs = [list(map(int, input().split())) for _ in range(n)]
dp = [[[n+3 for _ in range(rg+1)] for _ in range(ri+1)] for _ in range(n)]
dp[0][ri][rg] = 0
dp[0][max(ri-probs[0][0], 0)][max(rg-probs[0][1], 0)] = 1
for i in range(1, n):
    a, b = probs[i]
    for j in range(ri+1):
        for k in range(rg+1):
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
            dp[i][max(j-a, 0)][max(k-b, 0)] = min(dp[i][max(j-a, 0)][max(k-b, 0)], dp[i-1][j][k] + 1)
print(dp[-1][0][0] if dp[-1][0][0] != n+3 else -1)