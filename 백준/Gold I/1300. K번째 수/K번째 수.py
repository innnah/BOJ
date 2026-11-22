import sys
input = sys.stdin.readline

def solve(n, k):
    def f(x):
        cnt = 0
        minus = 0
        for i in range(1, n+1):
            cnt += min(x // i, n)
            if x % i == 0 and x // i <= n:
                minus += 1
        return [cnt - minus, cnt]
    
    lo, hi = 1, n*n
    while lo < hi:
        mid = (lo + hi) // 2
        cnt, cnt2 = f(mid)
        cnt2 -= 1
        #print(lo, hi, mid, cnt, cnt2)
        if cnt > cnt2 and cnt == k:
            lo = mid + 1
            continue
        if cnt <= k <= cnt2:
            return mid
        elif k < cnt:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

n = int(input())
k = int(input())
print(solve(n, k-1))