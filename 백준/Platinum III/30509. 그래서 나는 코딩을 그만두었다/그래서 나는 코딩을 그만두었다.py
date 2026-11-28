import sys
input = sys.stdin.readline

def f(x):
    mental = mb+r*x
    matched = [0 for _ in range(n)]
    left = n-x
    idx = 0
    while left > 0 and idx < n and sum(arr[idx]) < ma+mental:
        if arr[idx][0] > ma:
            mental += arr[idx][0] - ma
            matched[idx] = 1
            left -= 1
        idx += 1
    idx = 0
    while left > 0 and idx < n and sum(arr[idx]) < ma+mental:
        if not matched[idx]:
            matched[idx] = 1
            left -= 1
        idx += 1
    a = list(filter(lambda x : not matched[x[0]], enumerate(arr)))
    a.sort(key = lambda x : -x[1][0])
    for i in range(left):
        mental -= l + max(ma - a[i][1][0], 0)
    return mental > 0

n, l, r = map(int, input().split())
ma, mb = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : x[0] + x[1])
lo, hi = 0, n
while lo < hi:
    mid = (lo+hi)//2
    if f(mid):
        hi = mid
    else:
        lo = mid+1
print(n-lo)