import sys
input = sys.stdin.readline

def merge(a, b):
    if a == 0: return b
    if b == 0: return a
    return [a[0]+b[0], max(a[1], a[0]+b[1]), max(b[2], b[0]+a[2]), max(a[3], b[3], a[2]+b[1])]

def query(l, r, v, s, e):
    if r < s or e < l: return 0
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

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
tree = [[0, 0, 0, 0] for _ in range(n*4+8)]
for i in range(n):
    update(i, arr[i], 1, 0, n-1)
for _ in range(q):
    a, b = map(int, input().split())
    res = query(a-1, b-1, 1, 0, n-1)
    print(res[3])