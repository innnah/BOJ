import sys, heapq
input = sys.stdin.readline

INF = 98765432123456789
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, 0))
    distance[start][0] = 0
    while q:
        dist, node, paved = heapq.heappop(q)
        if distance[node][paved] < dist:
            continue
        for ne in graph[node]:
            cost = distance[node][paved] + ne[1]
            if cost < distance[ne[0]][paved]:
                distance[ne[0]][paved] = cost
                heapq.heappush(q, (cost, ne[0], paved))
            cost_paved = distance[node][paved]
            if paved != k and cost_paved < distance[ne[0]][paved+1]:
                distance[ne[0]][paved+1] = cost_paved
                heapq.heappush(q, (cost_paved, ne[0], paved+1))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [[INF] * (k+1) for _ in range(n+1)]
dijkstra(1)
print(min(distance[n]))