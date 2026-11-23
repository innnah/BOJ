import sys
input = sys.stdin.readline

dp = [[0] * 10 for _ in range(1001)]
dp[1] = [1] * 10
previousNum = [
    [7],
    [2, 4],
    [1, 3, 5],
    [2, 6],
    [1, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 9],
    [0, 4, 8],
    [5, 7, 9],
    [6, 8]
]
ret = [0 for _ in range(1001)]
ret[1] = 10
for i in range(2, 1001):
    for j in range(10):
        for k in previousNum[j]:
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= 1234567
        ret[i] += dp[i][j]
    ret[i] %= 1234567
for _ in range(int(input())):
    n = int(input())
    print(ret[n])