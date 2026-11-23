import sys, heapq
input = sys.stdin.readline

INF = 98765432123456789
def dijkstra(start, mode):
    distance = [INF for _ in range(n)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dis, node = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for ne in graph[node]:
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]] and \
            (mode or not dist[s][node] + ne[1] + dist[ne[0]][e] == dist[s][e]):
                distance[ne[0]] = cost
                heapq.heappush(q, (cost, ne[0]))
    return distance
while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    s, e = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
    dist = [[] for _ in range(n)]
    for i in range(n):
        dist[i] = dijkstra(i, 1)
    ret = dijkstra(s, 0)
    if ret[e] >= INF:
        print(-1)
    else:
        print(ret[e])