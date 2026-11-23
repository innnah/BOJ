import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def topology_sort():
    ret = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        var = q.popleft()
        ret.append(str(var))
        for i in graph[var]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return ret

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(' '.join(topology_sort()))