import sys
input = sys.stdin.readline

INF = float('inf')
def bellman_ford(start):
    dist[start] = 0
    for _ in range(n-1):
        for i in range(1, n+1):
            for j, d in graph[i]:
                dist[j] = min(dist[j], dist[i]+d)
    for i in range(1, n+1):
        for j, d in graph[i]:
            if dist[i] < INF and dist[i]+d < dist[j]:
                return True
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
minus_cycle = bellman_ford(1)
if minus_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] >= INF:
            print(-1)
        else:
            print(dist[i])