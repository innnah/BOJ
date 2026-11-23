import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    ret = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        if len(q) > 1:
            return ['?']
        v = q.popleft()
        ret.append(v)
        for i in range(1, n+1):
            if not graph[v][i]: continue
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return ret

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    indegree = [0 for _ in range(n+1)]
    graph = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            graph[l[i]][l[j]] = 1
            indegree[l[j]] += 1
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[b][a] = 1
            graph[a][b] = 0
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[b] += 1
            indegree[a] -= 1
    result = topology_sort()
    if len(result) < n: 
        print("IMPOSSIBLE")
    elif result[0] == "?":
        print("?")
    else:
        print(*result)