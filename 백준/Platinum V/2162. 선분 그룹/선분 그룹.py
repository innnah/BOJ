import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    s = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0])
    if s > 0: return 1
    if s == 0: return 0
    return -1

def isIntersect(l1, l2):
    p1, p2, p3, p4 = l1[0], l1[1], l2[0], l2[1]
    p1p2 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    p3p4 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if p1p2 == 0 and p3p4 == 0:
        if p1 > p2: p1, p2 = p2, p1
        if p3 > p4: p3, p4 = p4, p3
        return p3 <= p2 and p1 <= p4
    return p1p2 <= 0 and p3p4 <= 0

def find(v):
    if unionfind[v] == v: return v
    unionfind[v] = find(unionfind[v])
    return unionfind[v]

def union(u, v):
    r1, r2 = find(u), find(v)
    unionfind[r1] = r2
    size[r2] += size[r1]
    size[r1] = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [[arr[i][:2], arr[i][2:]] for i in range(n)]
unionfind = [i for i in range(n)]
size = [1 for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if find(i) == find(j): continue
        if isIntersect(arr[i], arr[j]): union(i, j)
res = 0
for i in range(n):
    if size[i] != 0:
        res += 1
print(res)
print(max(size))