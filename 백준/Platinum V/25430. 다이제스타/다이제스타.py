import sys, heapq
input = sys.stdin.readline

INF = float('inf')
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, 0))
    distance[start][0] = 0
    while q:
        dist, node, prev = heapq.heappop(q)
        no = d[prev]
        if distance[node][no] < dist:
            continue
        for ne in graph[node]:
            if ne[1] <= prev: continue
            cost = distance[node][no] + ne[1]
            new_no = d[ne[1]]
            if cost < distance[ne[0]][new_no]:
                distance[ne[0]][new_no] = cost
                heapq.heappush(q, (cost, ne[0], ne[1]))
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF] * (m+1) for _ in range(n+1)]
l = []
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    l.append(c)
l.sort()
d = {0 : 0}
for i in range(m):
    d[l[i]] = i+1
s, e = map(int, input().split())
dijkstra(s)
ret = min(distance[e])
if ret != INF:
    print(ret)
else:
    print("DIGESTA")