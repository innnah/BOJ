import sys
input = sys.stdin.readline
sys.setrecursionlimit(255000)

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
def canGo(a, b, c):
    if (lca(a,c)==c and lca(b,c)==lca(a,b)) or (lca(b,c)==c and lca(a,c)==lca(a,b)):
        return False
    else:
        return True

n = int(input())
LOG = 18
parent = [[0] * LOG for _ in range(n+1)]
d = [0 for _ in range(n+1)]
c = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
set_parent()
q = int(input())
for _ in range(q):
    a, *l = list(map(int, input().split()))
    if a == 1:
        i, j, k = l
        if canGo(i, j, k):
            print("YES")
        else:
            print("NO")
    else:
        i, j, k, l = l
        if not canGo(i, j, k) and not canGo(i, j, l):
            print("NO")
        else:
            print("YES")