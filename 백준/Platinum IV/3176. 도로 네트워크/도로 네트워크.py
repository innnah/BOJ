import sys
input = sys.stdin.readline
sys.setrecursionlimit(110000)

def dfs(v, depth):
    c[v] = 1
    d[v] = depth
    for i, dist in graph[v]:
        if c[i]: continue
        parent[i][0] = v
        minimum[i][0] = dist
        maximum[i][0] = dist
        dfs(i, depth+1)
def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
            minimum[j][i] = min(minimum[j][i-1], minimum[parent[j][i-1]][i-1])
            maximum[j][i] = max(maximum[j][i-1], maximum[parent[j][i-1]][i-1])
def lca(a, b):
    if d[a] > d[b]: a, b = b, a
    mini, maxi = 987654321, -987654321
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            mini = min(mini, minimum[b][i])
            maxi = max(maxi, maximum[b][i])
            b = parent[b][i]
    if a == b: return mini, maxi
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            mini = min([mini, minimum[b][i], minimum[a][i]])
            maxi = max([maxi, maximum[b][i], maximum[a][i]])
            a = parent[a][i]
            b = parent[b][i]
    return min(mini, minimum[a][0], minimum[b][0]), max(maxi, maximum[a][0], maximum[b][0])

n = int(input())
LOG = 21
parent = [[0] * LOG for _ in range(n+1)]
minimum = [[0] * LOG for _ in range(n+1)]
maximum = [[0] * LOG for _ in range(n+1)]
d = [0 for _ in range(n+1)]
c = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))
set_parent()
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(*lca(a,b))