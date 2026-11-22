import sys
from collections import deque
input=sys.stdin.readline
dx=[0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0 <= x < m and 0 <= y < n
def bfs():
    q = deque([(0, 0, 1, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, d, b = q.popleft()
        if x == m-1 and y == n-1: return d
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny):
                if l[ny][nx] == '1' and not b and not visited[ny][nx][1]:
                    visited[ny][nx][1] = 1
                    q.append((nx, ny, d+1, 1))
                if l[ny][nx] == '0' and not visited[ny][nx][b]:
                    visited[ny][nx][b] = 1
                    q.append((nx, ny, d+1, b))
    return -1

n,m = map(int, input().split())
l = [input().rstrip() for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(bfs())