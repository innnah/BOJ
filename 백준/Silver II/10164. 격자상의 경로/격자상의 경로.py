n, m, k = map(int, input().split())
if k == 0:
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i != j or i != 1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n][m])
else:
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    k -= 1
    row_k, column_k = k // m, k % m
    for i in range(1, row_k+2):
        for j in range(1, column_k+2):
            if i != j or i != 1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(row_k+1, n+1):
        for j in range(column_k+1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n][m])