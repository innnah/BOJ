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
            mst.append((u, ve))
            dist += w
            edges += 1
    return dist, mst
n = int(input())
graph = []
unionfind = [i for i in range(n+1)]
mst = []
for i in range(1, n):
    l = list(map(int, input().split()))
    for j in range(i+1, n+1):
        graph.append((i, j, l[j-i-1]))
graph.sort(key=lambda x:-x[2])
ret = kruskal()[1]
realgraph = [[] for _ in range(n+1)]
for i in ret:
    realgraph[i[0]].append(i[1])
    realgraph[i[1]].append(i[0])
for i in range(1, n+1):
    realgraph[i].sort()
    print(len(realgraph[i]), *realgraph[i])