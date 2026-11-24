from collections import deque
import sys
input = sys.stdin.readline
def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
order = []
for _ in range(m):
    a, *l = list(map(int, input().split()))
    for i in range(1, len(l)):
        graph[l[i-1]].append(l[i])
        indegree[l[i]] += 1
    order.append(l)
ret = topology_sort()
for i in order:
    ne = 0
    for j in ret:
        if i[ne] == j: ne += 1
        if ne == len(i): break
    else:
        print(0)
        sys.exit(0)
for i in ret:
    print(i)