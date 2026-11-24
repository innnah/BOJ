import sys
input = sys.stdin.readline

def merge(a, b):
    if a == [0, -10**20, -10**20, -10**20]: return b
    if b == [0, -10**20, -10**20, -10**20]: return a
    return [a[0]+b[0], max(a[1], a[0]+b[1]), max(b[2], b[0]+a[2]), max(a[3], b[3], a[2]+b[1])]

def query(l, r, v, s, e):
    if r < l: return [0, 0, 0, 0]
    if r < s or e < l: return [0, -10**20, -10**20, -10**20]
    if l <= s <= e <= r:
        return tree[v]
    mid = (s + e) // 2
    ls = query(l, r, v*2, s, mid)
    rs = query(l, r, v*2+1, mid+1, e)
    return merge(ls, rs)

def update(idx, val, v, s, e):
    if idx < s or e < idx: return tree[v]
    if s == e:
        tree[v] = [val, val, val, val]
        return tree[v]
    mid = (s + e) // 2
    ls = update(idx, val, v*2, s, mid)
    rs = update(idx, val, v*2+1, mid+1, e)
    tree[v] = merge(ls, rs)
    return tree[v]

def getAns(x1, y1, x2, y2):
    return query(y1+1, x2-1, 1, 0, n-1)[0]+query(x1, y1, 1, 0, n-1)[2]+query(x2, y2, 1, 0, n-1)[1]

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
tree = [[0, -10**20, -10**20, -10**20] for _ in range(n*4+8)]
for i in range(n):
    update(i, arr[i], 1, 0, n-1)
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if y1 < x2:
        print(getAns(x1, y1, x2, y2))
    else:
        print(max(getAns(x1, y1, y1+1, y2), getAns(x1, x2-1, x2, y2), query(x2, y1, 1, 0, n-1)[3]))