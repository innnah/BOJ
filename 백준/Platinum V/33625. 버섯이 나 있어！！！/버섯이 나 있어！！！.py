import sys
input = sys.stdin.readline

def f(x):
    cnt = [0 for _ in range(32)]
    for i in range(x):
        for j in range(32):
            if not (arr[i] & (1 << j)):
                cnt[j] += 1
    if min(cnt) > 0: return True
    for i in range(x, n):
        for j in range(32):
            if not (arr[i-x] & (1 << j)):
                cnt[j] -= 1
            if not (arr[i] & (1 << j)):
                cnt[j] += 1
        if min(cnt) > 0: return True
    return False

n = int(input())
arr = list(map(int, input().split()))
if not f(n):
    print(-1)
    sys.exit(0)
if f(1):
    print(n-arr.count(0))
    sys.exit(0)
lo, hi = 1, n
while lo < hi:
    mid = (lo + hi) // 2
    if f(mid):
        hi = mid
    else:
        lo = mid+1
print(lo-1+n-1)