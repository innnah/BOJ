import sys
input = sys.stdin.readline

def query(v, s, e, l, r):
    if r < s or e < l:
        return 0
    if l <= s <= e <= r:
        return seg[v]
    mid = (s + e) // 2
    return query(v*2, s, mid, l, r) + query(v*2+1, mid+1, e, l, r)
def update(v, s, e, idx, val):
    if idx < s or e < idx: return seg[v]
    if s == e:
        seg[v] += val
        return seg[v]
    mid = (s + e) // 2
    seg[v] = update(v*2, s, mid, idx, val) + update(v*2+1, mid+1, e, idx, val)
    return seg[v]

n = int(input())
tmp_arr = list(map(int, input().split()))
sarr = sorted(list(set(tmp_arr)))
d = {sarr[i] : i for i in range(len(sarr))}
arr = [d[x] for x in tmp_arr]

former = [n for _ in range(len(sarr))]
nxt = [-1 for _ in range(n)]
for i in range(n-1, -1, -1):
    nxt[i] = former[arr[i]]
    former[arr[i]] = i

q = int(input())
querys = [list(map(int, input().split())) + [i] for i in range(q)]
for i in range(q):
    querys[i][0] -= 1
    querys[i][1] -= 1
querys.sort()

seg = [0 for _ in range(1<<21)]
ans = [0 for _ in range(q)]
for i in range(len(sarr)):
    update(1, 0, n-1, former[i], 1)
j = 0
for i in range(q):
    l, r, idx = querys[i]
    for k in range(j, l):
        update(1, 0, n-1, nxt[k], 1)
    ans[idx] = query(1, 0, n-1, l, r)
    j = l
print('\n'.join(map(str, ans)))