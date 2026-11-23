import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0 for _ in range(n+2)] for _ in range(n+1)]
dp[0][1] = a[0]
for i in range(1, n):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i], dp[i-2][j-2] + b[i-1] + a[i-1] + a[i] if j-2 >= 0 else 0)
for i in range(1, n+1):
    print(dp[n-1][i])