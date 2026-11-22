import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dpf(idx, le, ri):
    if idx == n:
        return int(le == l and ri == r)
    ret = dp[idx][le][ri]
    if ret != -1: return ret
    ret = dpf(idx+1, le+1, ri)+(idx-1)*dpf(idx+1, le, ri)+dpf(idx+1, le, ri+1)
    dp[idx][le][ri] = ret
    return ret

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    dp = [[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
    print(dpf(1, 1, 1))