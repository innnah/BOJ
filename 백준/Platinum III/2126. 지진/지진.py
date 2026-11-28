import sys
input = sys.stdin.readline

def f(x):
    def find(v):
        if unionfind[v] == v: return v
        unionfind[v] = find(unionfind[v])
        return unionfind[v]
    def union(u, v):
        r1, r2 = find(u), find(v)
        unionfind[r2] = r1
    unionfind = [i for i in range(n+1)]
    edges.sort(key = lambda x2 : x2[3]*x+x2[2])
    cnt = 0
    s = 0
    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            union(edge[0], edge[1])
            cnt += 1
            s += edge[2] + edge[3]*x
        if cnt == n-1:
            break
    return s <= k

n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
lo, hi = -1, k
for _ in range(100):
    mid = (lo + hi) / 2
    if f(mid):
        lo = mid
    else:
        hi = mid
mid = (lo+hi)/2
if mid < 0:
    print("0.0000")
else:
    print("%.4f" % mid)