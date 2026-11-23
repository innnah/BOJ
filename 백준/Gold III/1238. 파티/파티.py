import sys, heapq

input = sys.stdin.readline

INF = 987654321
def dijkstra(start, graph, distance):
    q = []
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

n, m, x = map(int, input().split())
distance1 = [INF for _ in range(n+1)]
distance2 = [INF for _ in range(n+1)]
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph1[a].append((b, c))
    graph2[b].append((a, c))
dijkstra(x, graph1, distance1)
dijkstra(x, graph2, distance2)
ma = 0
for i in range(1, n+1):
    ma = max(ma, distance1[i]+distance2[i])
print(ma)