import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1

n, q = map(int, input().split())
unionfind = [i for i in range(n)]
logs = [list(map(int, input().split())) + [i] for i in range(n)]
logs.sort()
px1, px2, _, pidx = logs[0]
for i in range(1, n):
    x1, x2, _, idx = logs[i]
    if px2 >= x1:
        union(pidx, idx)
    if x2 >= px2:
        px1, px2, pidx = x1, x2, idx
for _ in range(q):
    a, b = map(int, input().split())
    print(f"{int(find(a-1) == find(b-1))}\n")