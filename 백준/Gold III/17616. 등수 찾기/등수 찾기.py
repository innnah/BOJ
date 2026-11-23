import sys

input = sys.stdin.readline

def dfs(graph, v):
    global visited
    cnt = 1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += dfs(graph, i)
    return cnt

n, m, x = map(int, input().split())
h = [[] for _ in range(n+1)]
l = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    h[b].append(a)
    l[a].append(b)
print(dfs(h, x), end = ' ')
visited = [False for _ in range(n+1)]
print(n - dfs(l, x) + 1)