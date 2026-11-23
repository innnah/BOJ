import sys, heapq
input = sys.stdin.readline

INF = 98765432123456789
def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for ne in graph[node]:
            if set([node, ne[0]]) == blocked: continue
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                trace[ne[0]] = node
                heapq.heappush(q, (cost, ne[0]))
    return distance
def reconstruct(v):
    path = [v]
    tmp = trace[v]
    while tmp != n:
        path.append(tmp)
        tmp = trace[tmp]
    path.append(n)
    return path

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
trace = [0 for _ in range(n+1)]
blocked = set()
distance = dijkstra(n)
track = reconstruct(1)
ret = 0
for i in range(1, len(track)):
    blocked = set([track[i-1], track[i]])
    tmp = dijkstra(1)
    ret = max(ret, tmp[n])
print(ret)