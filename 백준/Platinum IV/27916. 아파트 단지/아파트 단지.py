import sys, bisect
input = sys.stdin.readline

def f(x):
    dp = [0 for _ in range(n+1)]
    psum = [0 for _ in range(n+2)]
    dp[0] = 1
    psum[0] = 1
    for i in range(1, n+1):
        idx = bisect.bisect_left(arr, arr[i-1]-x)
        dp[i] = int(bool(psum[i-m]-psum[idx-1]) and i-m >= idx)
        psum[i] = psum[i-1] + dp[i]
    return dp[n]

n, m, q = map(int, input().split())
arr = list(map(int, input().split()))
querys = list(map(int, input().split()))
lo, hi = 0, 10**10
while lo < hi:
    mid = (lo+hi)//2
    if f(mid):
        hi = mid
    else:
        lo = mid+1
for i in querys:
    if lo <= i:
        print(1, end='')
    else:
        print(0, end='')