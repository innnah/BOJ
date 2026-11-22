import sys
input = sys.stdin.readline

n, l, m = map(int, input().split())
arr = input().rstrip().split()
length = len(arr[0])
if l < length:
    print(n**l)
    exit(0)
pos = [[0 for _ in range(m)] for _ in range(m)]
for i in range(m):
    for j in range(m):
        if arr[i][1:] == arr[j][:-1]:
            pos[i][j] = 1

dp = [[0 for _ in range(m)] for _ in range(l-length+1)]
for i in range(m):
    dp[0][i] = 1
for i in range(1, l-length+1):
    for j in range(m):
        for k in range(m):
            if pos[k][j]:
                dp[i][j] += dp[i-1][k]
print(sum(dp[-1]))