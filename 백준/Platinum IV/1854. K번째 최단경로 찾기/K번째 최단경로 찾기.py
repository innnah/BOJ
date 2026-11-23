import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start].append((0, 0))
    while q:
        dist, node = heapq.heappop(q)
        for ne in graph[node]:
            cost = dist + ne[1]
            if len(distance[ne[0]]) < k or cost < distance[ne[0]][0][1]:
                if len(distance[ne[0]]) == k:
                    heapq.heappop(distance[ne[0]])
                heapq.heappush(distance[ne[0]], (-cost, cost))
                heapq.heappush(q, (cost, ne[0]))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
dijkstra(1)
for i in range(1, n+1):
    if len(distance[i]) < k:
        print(-1)
    else:
        print(distance[i][0][1])