import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0<=x<n and 0<=y<m
def dfs(x, y):
    visited[x][y] = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and not visited[nx][ny] and board1[nx][ny] == board1[x][y]:
            dfs(nx, ny)

n, m = map(int, input().split())
board1 = [list(map(int, input().split())) for _ in range(n)]
board2 = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

diff = []
for i in range(n):
    for j in range(m):
        if board1[i][j] != board2[i][j]:
            diff.append((i, j))

if not diff:
    print("YES")
    sys.exit(0)

areas = [[] for _ in range(cnt)]
for i in range(n):
    for j in range(m):
        areas[visited[i][j]].append((i, j))
        
val = board2[diff[0][0]][diff[0][1]]
for i in diff:
    if board2[i[0]][i[1]] != val:
        print("NO")
        sys.exit(0)

for i in range(cnt):
    if diff == areas[i]:
        print("YES")
        break
else:
    print("NO")