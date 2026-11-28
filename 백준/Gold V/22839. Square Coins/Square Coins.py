dp = [[0 for _ in range(18)] for _ in range(301)]
dp[0][1] = 1
for i in range(1, 301):
    for j in range(1, 18):
        if i < j*j: break
        for k in range(1, j+1):
            dp[i][j] += dp[i-j*j][k]

while 1:
    n = int(input())
    if n == 0: break
    print(sum(dp[n]))