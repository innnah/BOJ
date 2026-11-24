import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, x = map(int, input().split())
    graph[u].append((v, x))
window = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

ngraph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    if window[i] == 0:
        dist = [10**20 for _ in range(n+1)]
        dijkstra(i)
        for j in range(1, n+1):
            if i == j: continue
            if window[j] == 0 and dist[j] <= a:
                ngraph[i].append((j, dist[j]))

dist = [10**20 for _ in range(n+1)]
q = [(0, 1)]
dist[1] = 0
while q:
    cost, node = heapq.heappop(q)
    if dist[node] < cost:
        continue
    state = cost % (a+b)
    for nxt, e_cost in ngraph[node]:
        if state + e_cost <= a:
            new_cost = cost + e_cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
        new_cost = cost + (a+b-state) + e_cost
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(q, (new_cost, nxt))
if dist[n] == 10**20:
    print(-1)
else:
    print(dist[n])