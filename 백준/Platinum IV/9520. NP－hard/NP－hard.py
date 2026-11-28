import sys
input = sys.stdin.readline

INF = 10**100
def dpf(left, right):
    idx = max(left, right)
    if idx == n-1:
        return 0
    if dp[left][right] != INF: return dp[left][right]
    dp[left][right] = min(dp[left][right], dpf(idx+1, right)+dist[idx+1][left], dpf(left, idx+1)+dist[right][idx+1])
    return dp[left][right]

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * (n+1) for _ in range(n+1)]
print(dpf(0, 0))