import sys, heapq

input = sys.stdin.readline

INF = 987654321
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for ne in graph[node]:
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                trace[ne[0]] = node
                heapq.heappush(q, (cost, ne[0]))

for i in range(int(input())):
    e, v = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance = [INF for _ in range(v)]
    trace = [0 for _ in range(v)]
    dijkstra(0)
    path = [v-1]
    tmp = trace[v-1]
    while tmp != 0:
        path.append(tmp)
        tmp = trace[tmp]
    path.append(0)
    print(f"Case #{i+1}: ", end = '')
    if distance[-1] != INF:
        print(*path[::-1])
    else:
        print(-1)