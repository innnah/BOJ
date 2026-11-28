import sys
input = sys.stdin.readline

def compress(l, r):
    length = r-l+1
    clength = r-l+1
    for i in range(1, length):
        if length % i != 0: continue
        ps = s[l:l+i]
        for j in range(i+l, r+1, i):
            if ps != s[j:j+i]: break
        else:
            clength = min(clength, len(str(length//i))+dp[l][l+i-1]+2)
    dp[l][r] = clength

s = input().rstrip()
n = len(s)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    dp[i][i] = 1
for i in range(2, n+1):
    for j in range(n-i+1):
        end = j+i-1
        compress(j, end)
        for k in range(j, end):
            dp[j][end] = min(dp[j][end], dp[j][k]+dp[k+1][end])
print(dp[0][n-1])