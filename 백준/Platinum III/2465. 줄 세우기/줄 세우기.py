import sys
input = sys.stdin.readline

def query(val, v, s, e):
    if s == e:
        return s
    mid = (s + e) // 2
    if tree[v*2] > val:
        return query(val, v*2, s, mid)
    else:
        return query(val-tree[v*2], v*2+1, mid+1, e)
def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] += val
        return tree[v]
    mid = (s + e) // 2
    tree[v] = update(idx, val, v*2, s, mid) + update(idx, val, v*2+1, mid+1, e)
    return tree[v]
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
d = {arr[i] : i for i in range(n)}
a = [d[i] for i in arr]
tree = [0 for _ in range(4*n+10)]
s = list(map(int, input().split()))
for i in range(n):
    update(a[i], 1, 1, 0, n-1)
ret = []
for i in range(n-1, -1, -1):
    v = query(s[i], 1, 0, n-1)
    ret.append(arr[v])
    update(v, -1, 1, 0, n-1)
for i in ret[::-1]:
    print(i)