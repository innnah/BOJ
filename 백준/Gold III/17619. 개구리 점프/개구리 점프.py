import sys
input = sys.stdin.readline
sys.setrecursionlimit(105000)

def find(v):
    if unionfind[v] == v:
        return v
    unionfind[v] = find(unionfind[v])
    return unionfind[v]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    unionfind[r2] = r1

n, q = map(int, input().split())
l = [tuple(map(int, input().split()))[:2] + (i+1,) for i in range(n)]
l.sort()
unionfind = [i for i in range(n+1)]
start, end, _ = l[0]
idx = 0
for i in range(1, n):
    if start <= l[i][0] <= l[i][1] <= end:
        union(l[i][2], l[idx][2])
    elif l[i][0] <= end:
        union(l[i][2], l[idx][2])
        end = l[i][1]
        idx = i
    else:
        start, end, _ = l[i]
        idx = i
for _ in range(q):
    a, b = map(int, input().split())
    print(int(find(a) == find(b)))