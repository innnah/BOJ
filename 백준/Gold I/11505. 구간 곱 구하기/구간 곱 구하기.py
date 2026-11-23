import sys
input = sys.stdin.readline

MOD = 10**9+7
def makeTree(v, s, e):
    if s == e:
        tree[v] = l[s-1]
        return tree[v]
    mid = (s+e)//2
    tree[v] = (makeTree(v*2, s, mid) * makeTree(v*2+1, mid+1, e)) % MOD
    return tree[v]
def query(v, s, e, le, ri):
    if le > e or ri < s: return 1
    if le <= s <= e <= ri:
        return tree[v]
    mid = (s+e)//2
    return (query(v*2, s, mid, le, ri) * query(v*2+1, mid+1, e, le, ri)) % MOD
def update(v, s, e, idx, val):
    if idx < s or idx > e: return tree[v]
    if s == e:
        tree[v] = val
        return tree[v]
    mid = (s+e)//2
    tree[v] = (update(v*2, s, mid, idx, val) * update(v*2+1, mid+1, e, idx, val)) % MOD
    return tree[v]
n, m, k = map(int, input().split())
l = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n*4+5)]
makeTree(1, 1, n)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, n, b, c)
    else:
        print(query(1, 1, n, b, c))