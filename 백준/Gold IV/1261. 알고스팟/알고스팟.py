import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0<=x<n and 0<=y<m
def bfs01():
    dq = deque([(0, 0, 0)])
    visited[0][0] = 1
    while dq:
        x, y, d = dq.popleft()
        if x == n-1 and y == m-1: return d
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny) and not visited[ny][nx]:
                visited[ny][nx] = 1
                if l[ny][nx] == 1:
                    dq.append((nx, ny, d+1))
                else:
                    dq.appendleft((nx, ny, d))

n, m = map(int, input().split())
l = [list(map(int, list(input().rstrip()))) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
print(bfs01())