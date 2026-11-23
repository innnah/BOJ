import sys
input = sys.stdin.readline

def find(u):
    while True:
        if u == unionfind[u]: break
        u = unionfind[u]
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1
n, m = map(int, input().split())
unionfind = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)