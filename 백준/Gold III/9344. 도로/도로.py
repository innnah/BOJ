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
        if edges == v-1: break
        u, ve, w = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            mst.append((u, ve))
            dist += w
            edges += 1
    return dist

for _ in range(int(input())):
    v, e, p, q = map(int, input().split())
    graph = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
    graph.sort(key = lambda x : -x[2])
    mst = []
    unionfind = [0]
    for i in range(1, v+1):
        unionfind.append(i)
    dist = kruskal()
    for i, j in mst:
        if (i == p and j == q) or (i == q and j == p): 
            print("YES")
            break
    else:
        print("NO")