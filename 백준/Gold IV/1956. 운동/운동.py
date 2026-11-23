import sys

input = sys.stdin.readline

INF = 987654321
cycle = INF
def floyd_warshall():
    global cycle
    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if i != j: cycle = min(cycle, dist[i][k]+dist[k][j]+dist[j][i])

n, m = map(int, input().split())
dist = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
floyd_warshall()
print(cycle if cycle != INF else -1)