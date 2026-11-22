import sys
sys.setrecursionlimit(110000)
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = 1
    depths[v] = depth
    for i in graph[v]:
        if not visited[i]:
            parents[i][0] = v
            dfs(i, depth+1)
def lca(u, v):
    if depths[u] > depths[v]:
        u, v = v, u
    for i in range(16, -1, -1):
        if depths[v] - depths[u] >= (1 << i):
            v = parents[v][i]
    if u == v:
        return u
    for i in range(16, -1, -1):
        if parents[u][i] != parents[v][i]:
            u = parents[u][i]
            v = parents[v][i]
    return parents[u][0]

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [[0] * 17 for _ in range(n+1)]
depths = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
dfs(1, 0)
for i in range(1, 17):
    for j in range(1, n+1):
        parents[j][i] = parents[parents[j][i-1]][i-1]

m = int(input())
for _ in range(m):
    r, u, v = map(int, input().split())
    lca1 = lca(u, v)
    if lca(lca1, r) != lca1:
        print(lca1)
    else:
        lca2, lca3 = lca(u, r), lca(u, v)
        if lca2 == lca3:
            print(lca(v, r))
        else:
            print(lca2)