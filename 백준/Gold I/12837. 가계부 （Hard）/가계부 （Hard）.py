import sys
input = sys.stdin.readline

def query(v, s, e, le, ri):
    if le > e or ri < s: return 0
    if le <= s <= e <= ri:
        return tree[v]
    mid = (s+e)//2
    return query(v*2, s, mid, le, ri) + query(v*2+1, mid+1, e, le, ri)
def update(v, s, e, idx, val):
    if idx < s or idx > e: return tree[v]
    if s == e:
        tree[v] += val
        return tree[v]
    mid = (s+e)//2
    tree[v] = update(v*2, s, mid, idx, val) + update(v*2+1, mid+1, e, idx, val)
    return tree[v]
n, q = map(int, input().split())
tree = [0 for _ in range(n*4+5)]
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, n, b, c)
    else:
        print(query(1, 1, n, b, c))