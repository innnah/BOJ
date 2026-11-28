import sys
from collections import deque
input = sys.stdin.readline

def isInside(x, y): return 0 <= x < n and 0 <= y < m
def bfs():
    q = deque()
    for i in range(m):
        if board[0][i]:
            q.append([0, i, 0])
    while q:
        x, y, d = q.popleft()
        if x == n-1:
            return d
        for i in range(k):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny) and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny, d+1])
    return -1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = []
dy = []
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    dx.append(a)
    dy.append(b)
visited = [[0 for _ in range(m)] for _ in range(n)]
print(bfs())