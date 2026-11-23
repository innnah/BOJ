import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1
def kruskal():
    global graph2
    edges = 0
    dist = 0
    while True:
        if edges == v-1: break
        u, ve, w = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            graph2[u].append((ve, w))
            graph2[ve].append((u, w))
            dist += w
            edges += 1
    return dist
def dfs(v, cur):
    global maxDist, maxNode
    visited[v] = 1
    dist = 0
    for node, cost in graph2[v]:
        if not visited[node]:
            dist = max(dfs(node, cur+cost) + cost, dist)
    if dist == 0 and cur >= maxDist:
        maxDist = cur
        maxNode = v 
    return dist

v, e = map(int, input().split())
graph = []
graph2 = [[] for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
graph.sort(key = lambda x : -x[2])
unionfind = [i for i in range(v)]
visited = [0 for _ in range(v)]
print(kruskal())
maxDist = -1
maxNode = -1
dfs(0, 0)
visited = [0 for _ in range(v)]
print(dfs(maxNode, 0))