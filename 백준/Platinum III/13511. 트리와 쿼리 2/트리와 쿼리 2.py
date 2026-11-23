import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, depth, dis):
    c[v] = 1
    d[v] = depth
    dist[v] = dis
    for i, a in graph[v]:
        if c[i]: continue
        parent[i][0] = v
        dfs(i, depth+1, dis+a)
def set_parent():
    dfs(1, 0, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
def lca(a, b):
    if d[a] > d[b]: a, b = b, a
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    if a == b: return a
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

n = int(input())
LOG = 21
parent = [[0] * LOG for _ in range(n+1)]
d = [0 for _ in range(n+1)]
c = [0 for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))
set_parent()
for _ in range(int(input())):
    query = list(map(int, input().split()))
    v = lca(query[1], query[2])
    if query[0] == 1:
        print(abs(dist[query[1]]-dist[v])+abs(dist[query[2]]-dist[v]))
    else:
        if abs(d[query[1]]-d[v]) >= query[3]:
            depth = query[3]-1
            node = query[1]
            for i in range(LOG - 1, -1, -1):
                if depth >= (1 << i):
                    node = parent[node][i]
                    depth -= (1 << i)
            print(node)
        elif abs(d[query[1]]-d[v]) < query[3]:
            depth = d[query[2]]-d[v] - (query[3] - (d[query[1]]-d[v]+1))
            node = query[2]
            for i in range(LOG - 1, -1, -1):
                if depth >= (1 << i):
                    node = parent[node][i]
                    depth -= (1 << i)
            print(node)