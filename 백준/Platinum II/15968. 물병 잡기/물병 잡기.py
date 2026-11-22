import sys
input = sys.stdin.readline

def f(mid):
    return -(mid+1) + (t//arr[mid])*arr[mid]

def bSearch_left(x):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if x < f(mid):
            lo = mid+1
        else:
            hi = mid
    return lo
def bSearch_right(x):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        val = f(mid)
        if x < val:
            lo = mid+1
        elif x > val:
            hi = mid
        else:
            return mid+1
    return lo

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
for i in range(1, n):
    arr[i] = arr[i-1] * ((arr[i]+arr[i-1]-1) // arr[i-1])
for _ in range(m):
    t, l, r = map(int, input().split())
    idx1, idx2 = bSearch_right(l), bSearch_left(r)
    print(idx1-idx2+(l <= t <= r))