import sys, heapq
sys.setrecursionlimit(20000)
input = sys.stdin.readline

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
                heapq.heappush(q, (cost, ne[0]))

def dpf(v):
    if v == 2:
        return 1
    if dp[v] != 0:
        return dp[v]
    ret = 0
    for i in graph[v]:
        if distance[v] > distance[i[0]]:
            ret += dpf(i[0])
    dp[v] = ret
    return ret

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [98765432123456789 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
dijkstra(2)
print(dpf(1))