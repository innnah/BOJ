import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dpf(idx, rolledLeft):
    if idx == n:
        return 0
    if dp[idx][rolledLeft] != -1: return dp[idx][rolledLeft]
    cur, res = (a[idx]+rolledLeft)%10, b[idx]
    le, ri = (res-cur+10)%10, (cur-res+10)%10
    suba, subb = le+dpf(idx+1, (rolledLeft+le)%10), ri+dpf(idx+1, rolledLeft)
    if suba > subb:
        trace[idx][rolledLeft] = -ri
    else:
        trace[idx][rolledLeft] = le
    dp[idx][rolledLeft] = min(suba, subb)
    return dp[idx][rolledLeft]
def reconstruct(idx, rolledLeft):
    if idx == n:
        return
    print(idx+1, trace[idx][rolledLeft])
    reconstruct(idx+1, (rolledLeft+max(0, trace[idx][rolledLeft])+10)%10)

n = int(input())
a = list(map(int, list(input().rstrip())))
b = list(map(int, list(input().rstrip())))
dp = [[-1] * 10 for _ in range(n)]
trace = [[-11] * 10 for _ in range(n)]
print(dpf(0, 0))
reconstruct(0, 0)