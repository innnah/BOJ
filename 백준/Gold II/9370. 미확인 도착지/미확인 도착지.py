import sys, heapq
input = sys.stdin.readline

INF = 98765432123456789
def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        for ne in graph[node]:
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                heapq.heappush(q, (cost, ne[0]))

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+2)]
    tmp = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        if a in (g,h) and b in (g,h) and a != b: tmp = c
        graph[a].append((b, c))
        graph[b].append((a, c))
    graph[n+1].append((g, 0))
    graph[n+1].append((h, 0))
    candidates = [int(input()) for _ in range(t)]
    candidates.sort()
    distance = [INF for _ in range(n+2)]
    distance2 = [INF for _ in range(n+2)]
    dijkstra(n+1, distance)
    dijkstra(s, distance2)
    for i in candidates:
        if distance[s] + distance[i] + tmp <= distance2[i]:
            print(i, end = ' ')
    print()