import sys, heapq
input = sys.stdin.readline

INF = 10**20
def dijkstra(s):
    q = [(0, s)]
    distance[s] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: continue
        for nxt in graph[node]:
            cost = distance[node] + nxt[1]
            if cost < distance[nxt[0]]:
                heapq.heappush(q, (cost, nxt[0]))
                distance[nxt[0]] = cost

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
s, e = map(int, input().split())
distance = [INF for _ in range(n+1)]
dijkstra(s)
print(distance[e])