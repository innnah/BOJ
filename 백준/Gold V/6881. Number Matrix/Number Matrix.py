import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0 <= x < m and 0 <= y < n
def bfs(a, b, c):
    visited[0] = [1 for _ in range(n)]
    q = deque()
    for i in range(n):
        q.append([0, i])
    while q:
        x, y = q.popleft()
        if x == m-1:
            return 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny) and not visited[nx][ny] and board[nx][ny] in (a, b, c):
                visited[nx][ny] = 1
                q.append([nx, ny])
    return 0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
for i in range(10):
    for j in range(i, 10):
        for k in range(j, 10):
            visited = [[0 for _ in range(n)] for _ in range(m)]
            if bfs(i, j, k):
                print(i, j, k)
                sys.exit(0)
print(-1, -1, -1)