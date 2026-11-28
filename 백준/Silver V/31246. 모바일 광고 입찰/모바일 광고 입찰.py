import sys
input = sys.stdin.readline

def achieved(v):
    cnt = 0
    for i in range(n):
        if arr[i][0] + v >= arr[i][1]:
            cnt += 1
    return cnt >= m

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
lo, hi = 0, 10**10
while lo < hi:
    mid = (lo + hi) // 2
    if achieved(mid):
        hi = mid
    else:
        lo = mid+1
print(lo)