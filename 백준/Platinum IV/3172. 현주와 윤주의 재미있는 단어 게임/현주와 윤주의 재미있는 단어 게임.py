import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

def query(v):
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    while idx <= n:
        tree[idx] += num
        idx += (idx & -idx)

n = int(input())
arr = [input().rstrip() for _ in range(n)]
rev_arr = [s[::-1] for s in arr]
d = {}
a = list(sorted(rev_arr))
for i in range(n):
    d[a[i][::-1]] = i+1
arr.sort()
tree = [0 for _ in range(n+1)]
ret = 0
for i in range(n):
    update(d[arr[i]], 1)
    ret += query(n) - query(d[arr[i]])
print(ret)