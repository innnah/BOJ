import sys
input = sys.stdin.readline

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1
def kruskal():
    edges = 0
    dist = 0
    while True:
        if edges == n-1: break
        u, ve, w = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            dist += w
            edges += 1
    return dist

n = int(input())
a = [[] for _ in range(n+1)]
unionfind = [i for i in range(n+1)]
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    a[0].append((x, y, z, i))
    a[1].append((x, y, z, i))
    a[2].append((x, y, z, i))
a[0].sort(key = lambda x:x[0])
a[1].sort(key = lambda x:x[1])
a[2].sort(key = lambda x:x[2])
graph = []
for i in range(1, n):
    for k in range(3):
        v = 987654321
        for j in range(3):
            v = min(v, abs(a[k][i][j]-a[k][i-1][j]))
        graph.append((a[k][i-1][3], a[k][i][3], v))
graph.sort(key = lambda x:-x[2])
print(kruskal())