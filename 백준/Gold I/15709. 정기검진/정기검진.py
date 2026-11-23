import sys, heapq
input = sys.stdin.readline

INF = 98765432123456789
def dijkstra(start):
    distance = [INF for _ in range(n+m+o+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        for ne in graph[node]:
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                heapq.heappush(q, (cost, ne[0]))
    return distance
n, m, o, k, q = map(int, input().split())
graph = [[] for _ in range(n+m+o+1)]
for i in range(n):
    graph[0].append((i+1, 0))
for _ in range(k):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dist = [[] for _ in range(o+1)]
for i in range(n+m+1, n+m+o+1):
    dist[i-n-m] = dijkstra(i)
for _ in range(q):
    x, y = map(int, input().split())
    ret = INF
    for i in range(1, o+1):
        ret = min(ret, dist[i][x] + dist[i][y])
    if ret < INF:
        print(ret)
    else:
        print(-1)