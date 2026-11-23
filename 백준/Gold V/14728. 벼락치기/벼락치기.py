import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]
l = [list(map(int, input().split())) for _ in range(n)]
if l[0][0] <= m: dp[1][l[0][0]] = l[0][1]

for i in range(2, n+1):
    if l[i-1][0] <= m: dp[i][l[i-1][0]] = l[i-1][1]
    for j in range(1, m+1):
        if dp[i-1][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j + l[i-1][0] <= m:
                dp[i][j+l[i-1][0]] = max(dp[i][j+l[i-1][0]], dp[i-1][j] + l[i-1][1])
maximum = 0
for i in dp:
    temp = max(i)
    maximum = max(maximum, temp)
print(maximum)