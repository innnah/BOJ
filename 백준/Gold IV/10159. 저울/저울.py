import sys
input = sys.stdin.readline

INF = 987654321
def floyd_warshall(dist):
    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
n = int(input())
m = int(input())
dist1 = [[INF] * (n+1) for _ in range(n+1)]
dist2 = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist1[a][b] = 1
    dist2[b][a] = 1
floyd_warshall(dist1)
floyd_warshall(dist2)
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if dist1[i][j] == INF and dist2[i][j] == dist1[i][j]:
            cnt += 1
    print(cnt)