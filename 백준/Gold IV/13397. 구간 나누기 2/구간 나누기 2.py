import sys
input = sys.stdin.readline

def f(x):
    pmn, pmx = 10**20, -10**20
    cnt = 1
    for i in range(n):
        pmn = min(pmn, arr[i])
        pmx = max(pmx, arr[i])
        if pmx - pmn > x:
            cnt += 1
            pmn = arr[i]
            pmx = arr[i]
    return cnt <= m

n, m = map(int, input().split())
arr = list(map(int, input().split()))
lo, hi = 0, sum(arr)
while lo < hi:
    mid = (lo + hi) // 2
    if f(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)