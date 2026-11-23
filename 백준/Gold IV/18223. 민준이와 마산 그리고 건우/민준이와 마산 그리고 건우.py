import sys, heapq

input = sys.stdin.readline

INF = 987654321
def dijkstra(start):
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

v, e, p = map(int, input().split())
distance = [INF for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1)
shortest = distance[-1]
toP = distance[p]
distance = [INF for _ in range(v+1)]
dijkstra(p)
print("SAVE HIM" if toP + distance[-1] == shortest else "GOOD BYE")