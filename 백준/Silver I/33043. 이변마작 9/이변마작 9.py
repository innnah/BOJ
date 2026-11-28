import sys
from collections import defaultdict
input = sys.stdin.readline

def f(x):
    d = defaultdict(int)
    for i in range(x):
        d[arr[i]] += 1
    for i in range(n-x):
        if max(list(d.values())) >= 5:
            return True
        d[arr[i]] -= 1
        d[arr[i+x]] += 1
    return max(list(d.values())) >= 5

n = int(input())
arr = input().rstrip().split()
lo, hi = 5, n+1
while lo < hi:
    mid = (lo + hi) // 2
    if f(mid):
        hi = mid
    else:
        lo = mid+1
if lo >= n+1:
    print(-1)
else:
    print(lo)