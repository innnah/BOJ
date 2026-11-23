import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, -2, 2, -1, 1]
def isInside(x, y): return 0<=x<size and 0<=y<size
def bfs():
    q = deque([(sx, sy, 0)])
    while q:
        x, y, d = q.popleft()
        if x == ex and y == ey: return d
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny) and not visited[ny][nx]:
                q.append((nx, ny, d+1))
                visited[ny][nx] = 1
for _ in range(int(input())):
    size = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * size for _ in range(size)]
    print(bfs())