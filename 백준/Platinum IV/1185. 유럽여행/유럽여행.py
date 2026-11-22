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
        w, u, ve = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            dist += w
            edges += 1
    return dist

n, m = map(int, input().split())
unionfind = [i for i in range(n+1)]
graph = []
arr = [int(input()) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c*2+arr[a-1]+arr[b-1], a, b))
graph.sort(reverse=True)
print(kruskal()+min(arr))