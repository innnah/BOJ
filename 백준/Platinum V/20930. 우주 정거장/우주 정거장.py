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
l = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    l.append([[a, b, c, d], [c, d, a, b]][(a, b) > (c, d)] + [i])
l_x = sorted(l, key = lambda x : (x[0], x[2]))
l_y = sorted(l, key = lambda x : (x[1], x[3]))
px1, _, px2, _, pidx = l_x[0]
for i in range(1, n):
    x1, _, x2, _, idx = l_x[i]
    if px1 <= x1 <= px2:
        union(pidx, idx)
    if x2 >= px2:
        px1, px2, pidx = x1, x2, idx
_, py1, _, py2, pidx = l_y[0]
for i in range(1, n):
    _, y1, _, y2, idx = l_y[i]
    if py1 <= y1 <= py2:
        if find(pidx) != find(idx): union(pidx, idx)
    if y2 >= py2:
        py1, py2, pidx = y1, y2, idx
for _ in range(q):
    a, b = map(int, input().split())
    print(f"{int(find(a-1) == find(b-1))}\n")