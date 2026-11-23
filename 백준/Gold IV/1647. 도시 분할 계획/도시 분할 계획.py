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
        if edges == v-2: break
        w, u, ve = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            dist += w
            edges += 1
    return dist
v, e = map(int, input().split())
graph = []
unionfind = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort(reverse=True)
print(kruskal())