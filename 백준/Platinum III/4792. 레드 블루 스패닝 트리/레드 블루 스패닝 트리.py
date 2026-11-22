import sys, heapq
input = sys.stdin.readline

def prim(start):
    pq = [(0, start)]
    dist = 0
    while pq:
        w, v = heapq.heappop(pq)
        if visited[v]: continue
        visited[v] = 1
        dist += w
        for p, we in graph[v]:
            if not visited[p]:
                heapq.heappush(pq, (we, p))
    return dist

while 1:
    n, m, k = map(int, input().split())
    if n == 0 and m == 0 and k == 0: break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = input().rstrip().split()
        b = int(b); c = int(c)
        a = int(a == "B")
        graph[b].append([c, a])
        graph[c].append([b, a])

    visited = [0 for _ in range(n+1)]
    ret1 = prim(1)
    for i in range(1, n+1):
        for j in range(len(graph[i])):
            graph[i][j][1] = int(not graph[i][j][1])
    visited = [0 for _ in range(n+1)]
    ret2 = n-1-prim(1)
    if ret1 <= k <= ret2:
        print(1)
    else:
        print(0)