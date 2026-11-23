import sys, heapq

input = sys.stdin.readline

INF = float('inf')
def dijkstra(start):
    distance = [INF for _ in range(v+1)]
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

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
d1, d2, d3 = dijkstra(1), dijkstra(v1), dijkstra(v2)
ret = min(d1[v1] + d2[v2] + d3[v], d1[v2] + d3[v1] + d2[v])
if ret < INF:
    print(ret)
else:
    print(-1)