import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < n
def dfs(x, y, c):
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and not visited[ny][nx] and p[ny][nx] == c:
            dfs(nx, ny, c)
n = int(input())
p = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(j, i, p[i][j])
            cnt += 1
print(cnt, end = ' ')
for i in range(n):
    for j in range(n):
        if p[i][j] == "G":
            p[i][j] = "R"
visited = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(j, i, p[i][j])
            cnt += 1
print(cnt)