import sys, bisect
sys.setrecursionlimit(127127)
input = sys.stdin.readline

MOD = 20070713
def dpf(idx):
    if idx == n: return 1
    if dp[idx] != -1: return dp[idx]
    dp[idx] = (dpf(idx+1) + dpf(go[idx])) % MOD
    return dp[idx]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
f = [arr[i][0] for i in range(n)]
go = [0 for _ in range(n)]
for i in range(n):
    idx = bisect.bisect(f, arr[i][1])
    go[i] = idx
dp = [-1 for _ in range(n)]
print(dpf(0))