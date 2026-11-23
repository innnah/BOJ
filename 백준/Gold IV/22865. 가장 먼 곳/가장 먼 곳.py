import sys, heapq

input = sys.stdin.readline

INF = float("inf")
def dijkstra(start):
    q = []
    distance = [INF for _ in range(v+1)]
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
v = int(input())
x, y, z = map(int, input().split())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
A, B, C = dijkstra(x), dijkstra(y), dijkstra(z)
minnum = 1
for i in range(1, v+1):
    if min(A[minnum], B[minnum], C[minnum]) < min(A[i], B[i], C[i]):
        minnum = i
print(minnum)