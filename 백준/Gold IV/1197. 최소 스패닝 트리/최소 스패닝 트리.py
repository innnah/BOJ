import heapq

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

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [0 for _ in range(n+1)]
print(prim(1))