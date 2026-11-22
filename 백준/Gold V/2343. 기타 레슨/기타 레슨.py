import sys
input = sys.stdin.readline

def f(x):
    cnt = 0
    cap = 0
    for i in range(n):
        if cap + arr[i] > x:
            cnt += 1
            cap = arr[i]
        else:
            cap += arr[i]
    cnt += 1
    return cnt <= m

n, m = map(int, input().split())
arr = list(map(int, input().split()))
lo, hi = max(arr), sum(arr)
while lo < hi:
    mid = (lo + hi) // 2
    if f(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)