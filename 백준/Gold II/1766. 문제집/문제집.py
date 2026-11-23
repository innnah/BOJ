import heapq, sys
input = sys.stdin.readline

def topology_sort():
    result = []
    q = []

    for i in range(1, v+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
    return result
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0 for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(*topology_sort())