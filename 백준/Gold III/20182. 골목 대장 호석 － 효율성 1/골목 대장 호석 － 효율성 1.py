import sys, heapq
input = sys.stdin.readline

INF = 987654321
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, start))
    distance[start][1] = 0
    distance[start][0] = 0
    while q:
        mdist, dist, node = heapq.heappop(q)
        if distance[node][0] < mdist:
            continue
        for ne in graph[node]:
            cost = distance[node][1] + ne[1]
            maxcost = max(distance[node][0], ne[1])
            if cost <= money and maxcost < distance[ne[0]][0]:
                distance[ne[0]][0] = maxcost
                distance[ne[0]][1] = cost
                heapq.heappush(q, (maxcost, cost, ne[0]))

n, m, s, e, money = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF, INF] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(s)
if distance[e][0] == INF:
    print(-1)
else:
    print(distance[e][0])