import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0<=x<n and 0<=y<n
def dfs(x, y):
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and arr[y][x] < arr[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(nx, ny)+1)
    return dp[y][x]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs(j, i)
print(max([max(i) for i in dp]))