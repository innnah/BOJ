import sys
input = sys.stdin.readline

def query(idx, v, s, e):
    if s == e: return s
    mid = (s+e)//2
    if idx > tree[v*2]:
        return query(idx-tree[v*2], v*2+1, mid+1, e)
    else:
        return query(idx, v*2, s, mid)

def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] += val
        return tree[v]
    mid = (s + e) // 2
    tree[v] = update(idx, val, v*2, s, mid) + update(idx, val, v*2+1, mid+1, e)
    return tree[v]

n, m = map(int, input().split())
gifts = list(map(int, input().split()))
want = list(map(int, input().split()))
kindness = list(map(int, input().split()))
tree = [0 for _ in range(400004)]
for i in range(n):
    update(gifts[i], 1, 1, 0, 100000)
for i in range(m):
    v = query(n-kindness[i]+1, 1, 0, 100000)
    if v < want[i]:
        print(0)
        break
    update(v, -1, 1, 0, 100000)
    update(v-want[i], 1, 1, 0, 100000)
else:
    print(1)