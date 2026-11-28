import sys
from itertools import combinations
input = sys.stdin.readline

def f(x, y):
    s = [0 for _ in range(b+1)]
    cnt = 0
    for i in range(n):
        for j in range(b+1):
            s[j] += psum[i][y[j]-1] - psum[i][y[j-1]-1]
        if max(s) > x:
            cnt += 1
            s = [0 for _ in range(b+1)]
            for j in range(b+1):
                s[j] += psum[i][y[j]-1] - psum[i][y[j-1]-1]
            if max(s) > x: return 0
    return cnt <= a

n, m = map(int, input().split())
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
c = list(combinations([i for i in range(1, m)], b))
psum = [[arr[i][0]] for i in range(n)]
for i in range(n):
    for j in range(1, m):
        psum[i].append(psum[i][-1]+arr[i][j])
    psum[i].append(0)
c = [list(i) for i in c]
res = 10**10
for comb in c:
    y = comb + [m, 0]
    lo, hi = 0, 10**8
    while lo < hi:
        mid = (lo+hi)//2
        if f(mid, y):
            hi = mid
        else:
            lo = mid+1
    res = min(res, lo)
print(res)