import sys
input = sys.stdin.readline

n = int(input())
values = [int(input()) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]

i, j = 1, n-1
cnt = 1
while j >= 1:
    if i == 1:
        dp[i][j] = dp[i][j+1] + cnt * values[j]
    elif j == n:
        dp[i][j] = dp[i-1][j] + cnt * values[cnt-1]
    else:
        dp[i][j] = max(dp[i][j+1] + cnt * values[j], dp[i-1][j] + cnt * values[i-2])
    if j == n:
        cnt += 1
        i, j = 1, n-cnt
    else:
        i += 1
        j += 1
maximum = 0
for i in range(1, n+1):
    maximum = max(maximum, dp[i][i] + values[i-1] * n)
print(maximum)