import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(1, n+1):
    if int(s[i-1]) > 0 :
        dp[i] += dp[i-1]
    if i > 1 and 10 <= int(s[i-2] + s[i-1]) <= 26:
        dp[i] += dp[i-2]
    dp[i] %= 1000000
print(dp[n])