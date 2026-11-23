import sys
input = sys.stdin.readline
sys.setrecursionlimit(7000)

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
LOG = 14
parent = [[0] * LOG for _ in range(n+1)]
d = [0 for _ in range(n+1)]
c = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
dfs_result = list(map(int, list(input().rstrip())))
stack = [0]
visited = [0 for _ in range(n+1)]
returned = [0 for _ in range(n+1)]
node_number = 1
for i in range(2*n):
    if not dfs_result[i]:
        graph[stack[-1]].append(node_number)
        stack.append(node_number)
        visited[node_number] = i+1
        node_number += 1
    else:
        returned[stack.pop()] = i+1
set_parent()
a, b = map(int, input().split())
try: a = visited.index(a)
except: a = returned.index(a)
try: b = visited.index(b)
except: b = returned.index(b)
v = lca(a, b)
print(visited[v], returned[v])