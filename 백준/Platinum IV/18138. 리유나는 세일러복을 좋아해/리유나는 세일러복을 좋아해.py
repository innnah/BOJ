import sys
input = sys.stdin.readline

def dfs(v):
    if visited[v]: return 0
    visited[v] = 1
    for i in graph[v]:
        if d[i] == -1 or dfs(d[i]):
            d[i] = v
            return 1
    return 0
n, m = map(int, input().split())
t_shirts = [int(input()) for _ in range(n)]
kara = [int(input()) for _ in range(m)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if t_shirts[i] * 0.5 <= kara[j] <= t_shirts[i] * 0.75 or t_shirts[i] <= kara[j] <= t_shirts[i] * 1.25:
            graph[i].append(j)
d = [-1 for _ in range(m)]
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
print(m-d.count(-1))