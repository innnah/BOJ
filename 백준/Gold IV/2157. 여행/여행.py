import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
dp = [[-1] * (m+1) for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a > b: continue
    graph[a][b] = max(graph[a][b], c)
dp[1][1] = 0
for i in range(2, n+1):
    for j in range(2, min(m, i)+1):
        for l in range(1, n+1):
            if graph[l][i] != 0 and l >= j-1 and dp[l][j-1] != -1:
                dp[i][j] = max(dp[l][j-1]+graph[l][i], dp[i][j])
print(max(dp[n]))