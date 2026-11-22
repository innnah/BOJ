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
    size[root1] += size[root2]

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key = lambda x:x[2])
unionfind = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]
cnt = n*(n-1)//2
ret = sum([i[2] for i in edges]) * cnt
for _ in range(m):
    edge = edges.pop()
    a, b = find(edge[0]), find(edge[1])
    if a != b:
        cnt -= size[a] * size[b]
        union(a, b)
    ret -= cnt * edge[2]
print(ret%(10**9))