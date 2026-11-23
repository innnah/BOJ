import sys, heapq
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
            if closed in [(node, ne[0]), (ne[0], node)]:
                continue
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                trace[ne[0]] = node
                heapq.heappush(q, (cost, ne[0]))
def reconstruct(v):
    path = [v]
    tmp = trace[v]
    while tmp != 0:
        path.append(tmp)
        tmp = trace[tmp]
    return path[::-1]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [987654321 for _ in range(n+1)]
trace = [0 for _ in range(n+1)]
closed = (0,0)
dijkstra(1)
path = reconstruct(n)
original = distance[n]
ret = 0
for i in range(len(path)-1):
    closed = (path[i], path[i+1])
    distance = [987654321 for _ in range(n+1)]
    dijkstra(1)
    ret = max(distance[n], ret)
if ret == 987654321:
    print(-1)
else:
    print(ret-original)