import sys
input = sys.stdin.readline

def f(x):
    ret = 0
    for i in range(n+1):
        ret += arr[i] * (x ** i)
    return ret

n = int(input())
arr = [float(input()) for _ in range(n+1)]
if arr[n] < 0:
    for i in range(n+1):
        arr[i] *= -1
lo, hi = -1000000, 1000000
while hi - lo > 1e-7:
    mid = (lo + hi) / 2
    if f(mid) > 0:
        hi = mid
    else:
        lo = mid
print(int(lo * 1000))