import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
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
n, m = map(int, input().split())
s = int(input())
graph = [[] for _ in range(n+1)]
distance = [987654321 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dijkstra(s)
for i in range(1, n+1):
    if distance[i] == 987654321: print("INF")
    else: print(distance[i])