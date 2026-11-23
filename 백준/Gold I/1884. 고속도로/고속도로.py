import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, start))
    distance[start][0] = 0
    while q:
        dist, payed, node = heapq.heappop(q)
        if distance[node][payed] < dist:
            continue
        for ne, time, cost in graph[node]:
            cand = distance[node][payed] + time
            if payed+cost <= money and cand < distance[ne][payed+cost]:
                distance[ne][payed+cost] = cand
                heapq.heappush(q, (cand, payed+cost, ne))

money = int(input())
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    graph[a].append((b,c,d))
distance = [[987654321] * (money+1) for _ in range(n+1)]
dijkstra(1)
ret = min(distance[n])
if ret != 987654321:
    print(ret)
else:
    print(-1)