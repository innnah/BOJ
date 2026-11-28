import sys, bisect
sys.setrecursionlimit(150000)
input = sys.stdin.readline

cnt = -1
def dfs(v, p):
    global cnt
    cnt += 1
    s[v] = cnt
    a = 0
    for i in tree[v]:
        if i != p:
            dfs(i, v)
            a += 1
    e[v] = cnt
    if not a: leaves.append(v)

def dfs2(v, p):
    global ans
    for i in tree[v]:
        if i != p:
            dfs2(i, v)
    for _ in range(spawn[v]):
        l, r = s[v], e[v]
        a, b = bisect.bisect_left(leaves, l), bisect.bisect(leaves, r)-1
        ret = query(1, 0, n-1, a, b)
        if ret != -1:
            ans += 1
            update(1, 0, n-1, ret)

def update(v, s, e, idx):
    if idx < s or e < idx:
        return seg[v]
    if s == e:
        seg[v] += 1
        return seg[v]
    mid = (s + e) // 2
    seg[v] = update(v*2, s, mid, idx) + update(v*2+1, mid+1, e, idx)
    return seg[v]

def query(v, s, e, l, r):
    if e < l or r < s: return -1
    if seg[v] == e-s+1: return -1
    if s == e: return s
    mid = (s + e) // 2
    ret1 = query(v*2, s, mid, l, r)
    if ret1 != -1: return ret1
    ret2 = query(v*2+1, mid+1, e, l, r)
    return ret2

n = int(input())
potions = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
s = [-1 for _ in range(n+1)]
e = [-1 for _ in range(n+1)]
leaves = []
dfs(1, -1)

leaves = [s[leaves[i]] for i in range(len(leaves))]
leaves.sort()

seg = [0 for _ in range(262145)]
ans = 0
spawn = [0 for _ in range(n+1)]
for i in range(len(leaves)):
    spawn[potions[i]] += 1
dfs2(1, -1)
print(ans)