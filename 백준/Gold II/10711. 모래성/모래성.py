import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, -1, 0, 1, -1, 0, 1]
def isInside(x, y): return 0<=x<n and 0<=y<m
n, m = map(int, input().split())
board = [list(map(int, input().rstrip().replace('.', '0'))) for _ in range(n)]
empty = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]:
            for k in range(8):
                nx, ny = i + dx[k], j + dy[k]
                if isInside(nx, ny) and not board[nx][ny]:
                    empty[i][j] += 1

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j]:
            if empty[i][j] >= board[i][j]:
                q.append([i, j])

cnt = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        board[x][y] = 0
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny) and board[nx][ny]:
                empty[nx][ny] += 1
                if empty[nx][ny] == board[nx][ny]:
                    q.append([nx, ny])
    cnt += 1
print(cnt)