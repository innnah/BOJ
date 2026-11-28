import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def tracking(a, b):
    if a >= 3 and dp[a-4][b] + arr[a] - arr[a-3] == dp[a][b]:
        return tracking(a-4, b)
    if b >= 1 and dp[a-1][b-1] == dp[a][b]:
        return tracking(a-1, b-1) + [idxs[a]]
    return []

n = int(input())
arr = list(map(int, input().split()))
arr = [[arr[i], i] for i in range(n)]
arr.sort()
idxs = [arr[i][1] for i in range(n)]
arr = [arr[i][0] for i in range(n)]

dp = [[10**20 for _ in range(4)] for _ in range(n+1)]
dp[-1][0] = 0
for i in range(n):
    for j in range(4):
        if i >= 3:
            dp[i][j] = min(dp[i][j], dp[i-4][j] + arr[i] - arr[i-3])
        if j >= 1:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1])
print(dp[n-1][n%4])
ans = tracking(n-1, n%4)
for i in ans:
    print(i)