n = int(input())
dp = [0] * 1001
if n == 1:
    print(0)
else:
    for i in range(2, n+1):
        if i % 2:
            dp[i] = 2 * dp[i-1] - 1
        else:
            dp[i] = 2 * dp[i-1] + 1
    print(dp[n])