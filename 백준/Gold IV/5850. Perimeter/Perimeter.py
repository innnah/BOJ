import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def isInside(x, y): return 0 <= x < 102 and 0 <= y < 102

n = int(input())
board = [[0 for _ in range(102)] for _ in range(102)]
for i in range(n):
    a, b = map(int, input().split())
    board[a][b] = 1

q = deque([(0, 0)])
visited = [[0 for _ in range(102)] for _ in range(102)]
visited[0][0] = 1
p = [[[0, 0, 0, 0] for _ in range(102)] for _ in range(102)]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and not visited[nx][ny]:
            if not board[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
            else:
                p[nx][ny][i] = 1
ans = 0
for i in range(102):
    for j in range(102):
        for k in range(4):
            ans += p[i][j][k]
print(ans)