import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < n
def dfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and not visited[ny][nx] and status[ny][nx]:
            dfs(nx, ny)

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
m = 0
for i in range(101):
    status = [[1] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if l[j][k] <= i: status[j][k] = 0
    cnt = 0
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and status[j][k]:
                dfs(k, j)
                cnt += 1
    m = max(m, cnt)
print(m)