import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, depth):
    c[v] = 1
    d[v] = depth
    for i in graph[v]:
        if c[i]: continue
        parent[i][0] = v
        dfs(i, depth+1)
def set_parent():
    dfs(1, 0)
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
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
set_parent()
ret = 0
prev = 1
m = int(input())
for _ in range(m):
    goto = int(input())
    v = lca(prev, goto)
    ret += abs(d[prev]-d[v]) + abs(d[v]-d[goto])
    prev = goto
print(ret)