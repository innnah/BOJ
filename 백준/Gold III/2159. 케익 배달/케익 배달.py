import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0]
dy = [-1, 1, 0, 0, 0]
n = int(input())
sx, sy = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.append([sx, sy])
dp = [[10**20 for _ in range(5)] for _ in range(n+1)]
dp[-1][4] = 0
for i in range(n):
    for j in range(5):
        x, y = arr[i][0]+dx[j], arr[i][1]+dy[j]
        for k in range(5):
            px, py = arr[i-1][0]+dx[k], arr[i-1][1]+dy[k]
            dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(x-px) + abs(y-py))
print(min(dp[n-1]))