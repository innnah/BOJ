import sys, heapq

input = sys.stdin.readline

INF = 987654321
def dijkstra(start):
    distance = [INF for _ in range(v+1)]
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
    return distance

n, v, e = map(int, input().split())
p1, p2 = map(int, input().split())
l = list(map(int, input().split()))
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dist1, dist2 = dijkstra(p1), dijkstra(p2)
s = 0
for i in l:
    s += dist1[i] + dist2[i]
print(s)