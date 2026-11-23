import sys, heapq

input = sys.stdin.readline

INF = float("INF")
def dijkstra(start):
    q = []
    distance = [INF for _ in range(v+1)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
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
x, z = map(int, input().split())
p = int(input())
dist1, dist2 = dijkstra(x), dijkstra(z)
m = list(map(int, input().split()))
shortest = INF
for ve in m:
    shortest = min(shortest, dist1[ve] + dist2[ve])
if shortest < INF:
    print(shortest)
else:
    print(-1)