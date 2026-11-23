import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n-1)]
dp[0][l[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        if 0 <= j - l[i] <= 20:
            dp[i][j-l[i]] += dp[i-1][j]
        if 0 <= j + l[i] <= 20:
            dp[i][j+l[i]] += dp[i-1][j]
print(dp[-1][l[-1]])