import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0 <= x < m and 0 <= y < n
def bfs():
    q = deque([[(0, 0), 1]])
    while q:
        v = q.popleft()
        x, y = v[0][0], v[0][1]
        if x == m-1 and y == n-1: return v[1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not isInside(nx, ny) or visited[ny][nx] or l[ny][nx] == '0': continue
            q.append([(nx, ny), v[1]+1])
            visited[ny][nx] = True

n, m = map(int, input().split())
l = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
print(bfs())