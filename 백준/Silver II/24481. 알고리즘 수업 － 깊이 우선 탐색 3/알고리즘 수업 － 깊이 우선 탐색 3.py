import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)

def dfs(v, d):
    visited[v] = d
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i, d+1)
n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
dfs(s, 0)
for i in range(1, n+1):
    print(visited[i])