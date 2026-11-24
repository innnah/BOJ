import sys, heapq
input = sys.stdin.readline

n, m, h = map(int, input().split())
h_holes = [list(map(int, input().split())) for _ in range(n+1)]
v_holes = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n*m+1)]
for i in range(m):
    if h_holes[0][i] != -1:
        graph[-1].append((i, h_holes[0][i]))
    if h_holes[n][i] != -1:
        graph[-1].append(((n-1)*m+i, h_holes[n][i]))
for i in range(n):
    if v_holes[i][0] != -1:
        graph[-1].append((i*m, v_holes[i][0]))
    if v_holes[i][m] != -1:
        graph[-1].append(((i+1)*m-1, v_holes[i][m]))
for i in range(1, n):
    for j in range(m):
        if h_holes[i][j] != -1:
            graph[(i-1)*m+j].append((i*m+j, h_holes[i][j]))
            graph[i*m+j].append(((i-1)*m+j, h_holes[i][j]))
for i in range(n):
    for j in range(1, m):
        if v_holes[i][j] != -1:
            graph[i*m+j-1].append((i*m+j, v_holes[i][j]))
            graph[i*m+j].append((i*m+j-1, v_holes[i][j]))
distance = [54321 for _ in range(n*m+1)]
pq = [(0, n*m)]
distance[-1] = 0
while pq:
    dist, v = heapq.heappop(pq)
    for i, d in graph[v]:
        cost = max(d, dist)
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(pq, (cost, i))
ret = 0
for i in distance:
    if i != 54321:
        ret += i
    else:
        ret += h
print(ret)