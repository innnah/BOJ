n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, 7):
        if i-j <= 0:
            dp[i] += 1 / 6
        else:
            dp[i] += (dp[i-j]+1) / 6
print(dp[n])