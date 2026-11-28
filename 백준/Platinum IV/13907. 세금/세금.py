import sys, heapq
input = sys.stdin.readline

INF = 10**100
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, start))
    distance[start][0] = 0
    while q:
        dist, passed, node = heapq.heappop(q)
        if passed == n:
            continue
        FlagTrue = 0
        for i in range(passed+1):
            if distance[node][i] < dist:
                FlagTrue = 1
                break
        if FlagTrue:
            continue
        for ne in graph[node]:
            cost = distance[node][passed] + ne[1]
            if cost < distance[ne[0]][passed+1]:
                distance[ne[0]][passed+1] = cost
                heapq.heappush(q, (cost, passed+1, ne[0]))

n, m, k = map(int, input().split())
s, d = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [[INF]*(n+1) for _ in range(n+1)]
dijkstra(s)
psum = 0
ret = INF
for i in range(n+1):
    ret = min(ret, distance[d][i]+psum*i)
print(ret)
for _ in range(k):
    psum += int(input())
    ret = INF
    for i in range(n+1):
        ret = min(ret, distance[d][i]+psum*i)
    print(ret)