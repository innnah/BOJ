import sys
input = sys.stdin.readline

def makeTree(v, s, e):
    if s == e:
        tree[v] = l[s]
        return tree[v]
    mid = (s + e) // 2
    tree[v] = makeTree(v*2, s, mid) + makeTree(v*2+1, mid+1, e)
    return tree[v]
def query(le, ri, v, s, e):
    if le > e or ri < s: return 0
    if le <= s <= e <= ri: return tree[v]
    mid = (s + e) // 2
    return query(le, ri, v*2, s, mid) + query(le, ri, v*2+1, mid+1, e)
def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] = val
        return tree[v]
    mid = (s + e) // 2
    tree[v] = update(idx, val, v*2, s, mid) + update(idx, val, v*2+1, mid+1, e)
    return tree[v]

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    tree = [0 for _ in range((n+m)*4+1)]
    place = [0 for _ in range(n+1)]
    for i in range(m, n+m):
        update(i, 1, 1, 0, n+m-1)
        place[i-m] = i
    idx = m-1
    for i in l:
        print(query(0, place[i-1]-1, 1, 0, n+m-1), end = ' ')
        update(place[i-1], 0, 1, 0, n+m-1)
        update(idx, 1, 1, 0, n+m-1)
        place[i-1] = idx
        idx -= 1
    print()