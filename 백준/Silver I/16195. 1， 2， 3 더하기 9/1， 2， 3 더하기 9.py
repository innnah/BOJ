import sys
input = sys.stdin.readline
MAX = 1000
MOD = 1000000009
dp = [[0] * (MAX+1) for _ in range(MAX+1)]
psum = [[0] * (MAX+1) for _ in range(MAX+1)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1
psum[1][1] = 1
psum[2][1] = 1
psum[2][2] = 2
psum[3][1] = 1
psum[3][2] = 3
psum[3][3] = 4
for i in range(4, MAX+1):
    for j in range(1, MAX+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD
        psum[i][j] = (psum[i][j-1] + dp[i][j]) % MOD
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(psum[n][m])