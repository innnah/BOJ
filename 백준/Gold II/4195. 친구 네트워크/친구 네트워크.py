import sys
from collections import defaultdict
input = sys.stdin.readline

def find(u):
    if unionfind.get(u) is None:
        return u
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1
    size[root1] += size[root2]
for _ in range(int(input())):
    n = int(input())
    unionfind = {}
    size = defaultdict(int)
    for _ in range(n):
        a, b = input().split()
        if size.get(a) is None:
            size[a] = 1
        if size.get(b) is None:
            size[b] = 1
        if find(a) != find(b):
            union(a, b)
        print(size[find(a)])