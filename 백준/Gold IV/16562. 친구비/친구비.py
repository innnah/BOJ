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
n, m, k = map(int, input().split())
unionfind = [i for i in range(n+1)]
l = list(map(int, input().split()))
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
ret = [[] for _ in range(n+1)]
for i in range(1, n+1):
    ret[find(i)].append(l[i-1])
need = 0
for i in range(1, n+1):
    if ret[i]:
        need += min(ret[i])
if k < need:
    print("Oh no")
else:
    print(need)