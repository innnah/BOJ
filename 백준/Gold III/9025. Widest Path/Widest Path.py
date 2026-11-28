import sys, heapq
input = sys.stdin.readline

def dijkstra():
    pq = [(-10**20, s)]
    distance[s] = -10**20
    while pq:
        dist, v = heapq.heappop(pq)
        if distance[v] < dist:
            continue
        for i, d in graph[v]:
            cost = max(dist, -d)
            if distance[i] > cost:
                heapq.heappush(pq, (cost, i))
                distance[i] = cost

for _ in range(int(input())):
    n, m, s, t = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance = [0 for _ in range(n+1)]
    dijkstra()
    print(-distance[t])