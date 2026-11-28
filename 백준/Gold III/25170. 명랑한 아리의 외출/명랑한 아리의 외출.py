import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 1]
dy = [1, 0, 1]
def isInside(x, y): return 0<=x<n and 0<=y<m

n, m, t = map(int, input().split())
works = [list(map(int, input().split())) for _ in range(n)]
wt = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-10**20 for _ in range(t+1)] for _ in range(m)] for _ in range(n)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(m):
        for time in range(1, t+1):
            for k in range(3):
                px, py = i - dx[k], j - dy[k]
                if isInside(px, py):
                    dp[i][j][time] = max(dp[i][j][time], dp[px][py][time-1])
                    if time - wt[i][j] - 1 >= 0:
                        dp[i][j][time] = max(dp[i][j][time], dp[px][py][time-wt[i][j]-1] + works[i][j])
print(max(dp[-1][-1]))