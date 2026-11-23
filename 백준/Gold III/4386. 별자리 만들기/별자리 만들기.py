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
        w, u, ve = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            dist += w
            edges += 1
    return dist

v = int(input())
l = [list(map(float, input().split())) for _ in range(v)]
unionfind = [i for i in range(v)]
graph = []
for i in range(v):
    for j in range(v):
        if i == j: continue
        x1, y1 = l[i]
        x2, y2 = l[j]
        graph.append((((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5, i, j))
graph.sort(reverse = True)
print(kruskal())