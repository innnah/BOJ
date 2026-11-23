import sys
input = sys.stdin.readline

def floyd_warshall():
    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

INF = 987654321
n = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
while 1:
    a, b = map(int, input().split())
    if a == -1: break
    dist[a][b] = 1
    dist[b][a] = 1
floyd_warshall()
ret = INF
l = []
for i in range(1, n+1):
    ret = min(ret, max(dist[i][1:]))
for i in range(1, n+1):
    if max(dist[i][1:]) == ret:
        l.append(i)
print(ret, len(l))
print(*l)