import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    psum = [0 for _ in range(n+1)]
    psum[0] = arr[0]
    for i in range(1, n):
        psum[i] = psum[i-1] + arr[i]

    dp = [[10**10 for _ in range(n)] for _ in range(n)]
    opt = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0
        opt[i][i] = i

    for diff in range(1, n):
        for i in range(n-diff):
            j = i+diff
            s = opt[i][j-1] if j > 0 else 0
            e = opt[i+1][j] if i+1 < n else n-2
            for k in range(s, min(e, j-1)+1):
                if dp[i][j] > dp[i][k] + dp[k+1][j] + psum[j] - psum[i-1]:
                    dp[i][j] = dp[i][k] + dp[k+1][j] + psum[j] - psum[i-1]
                    opt[i][j] = k
    print(dp[0][n-1])