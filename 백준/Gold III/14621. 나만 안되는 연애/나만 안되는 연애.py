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
        if len(graph) == 0:
            print(-1)
            sys.exit(0)
        u, ve, w = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            dist += w
            edges += 1
    return dist

v, e = map(int, input().split())
l = input().rstrip().split()
graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    if l[a-1] != l[b-1]:
        graph.append((a,b,c))
graph.sort(key = lambda x : -x[2])
unionfind = [0]
for i in range(1, v+1):
    unionfind.append(i)
print(kruskal())