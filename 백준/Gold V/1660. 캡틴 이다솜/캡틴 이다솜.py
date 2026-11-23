import sys

n = int(input())
INF = 300005
dp = [INF for _ in range(n+1)]
dp[0] = 0
uses = []
a = 0
for i in range(1, INF):
    a += i * (i+1) // 2
    if a > n: break
    uses.append(a)
for i in range(1, n+1):
    for j in uses:
        if j > i: break
        dp[i] = min(dp[i], dp[i-j]+1)
print(dp[n])