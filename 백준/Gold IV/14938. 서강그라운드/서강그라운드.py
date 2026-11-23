import sys

input = sys.stdin.readline

INF = 987654321
def floyd_warshall():
    for i in range(1, n+1):
        for j, d in graph[i]:
            dist[i][j] = d

    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n, m, r = map(int, input().split())
itemNum = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dist = [[INF] * (n+1) for _ in range(n+1)]
floyd_warshall()
maxItem = -1
for i in range(1, n+1):
    items = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:
            items += itemNum[j-1]
    maxItem = max(maxItem, items)
print(maxItem)