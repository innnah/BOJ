import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
dp = [[-98765432123456789] * 2 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][1] = max([0, dp[i-1][1], dp[i-2][0]]) + l[i-1]
    dp[i][0] = max(0, dp[i-1][0]) + l[i-1]
ret = -98765432123456789
for i in dp:
    ret = max(max(i), ret)
print(ret)