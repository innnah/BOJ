import sys, heapq
input = sys.stdin.readline

INF = 987654321
def dijkstra(start, state):
    q = []
    heapq.heappush(q, (0, start))
    distance[state][start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[state][node] < dist:
            continue
        for ne in graph[node]:
            cost = distance[state][node] + ne[1]
            if state == 0 and cost > x: continue
            if state == 1 and cost > y: continue
            if cost < distance[state][ne[0]]:
                distance[state][ne[0]] = cost
                heapq.heappush(q, (cost, ne[0]))

v, e = map(int, input().split())
distance = [[INF] * (v+2) for _ in range(2)]
graph = [[] for _ in range(v+2)]
house = [1 for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
m, x = map(int, input().split())
ms = list(map(int, input().split()))
for i in ms:
    graph[v+1].append((i, 0))
    house[i] = 0
dijkstra(v+1, 0)
s, y = map(int, input().split())
ss = list(map(int, input().split()))
graph[v+1] = []
for i in ss:
    graph[v+1].append((i, 0))
    house[i] = 0
dijkstra(v+1, 1)

ret = INF
for i in range(1, v+1):
    if not house[i]: continue
    ret = min(ret, distance[0][i] + distance[1][i])
if ret >= INF:
    print(-1)
else:
    print(ret)