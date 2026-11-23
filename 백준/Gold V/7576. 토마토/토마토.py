import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < m
def bfs():
    q = deque([])
    for i in tomatoes:
        q.append([i, 0])
        visited[i[1]][i[0]] = True
    while q:
        v = q.popleft()
        x, y = v[0][0], v[0][1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not isInside(nx, ny) or visited[ny][nx] or l[ny][nx] == -1: continue
            q.append([(nx, ny), v[1]+1])
            tomatoes.append((nx, ny))
            visited[ny][nx] = True
            if len(tomatoes) == allTomatoes: return v[1]+1
    return -1

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
tomatoes = []
allTomatoes = n*m
for i in range(m):
    for j in range(n):
        if l[i][j] == 1:
            tomatoes.append((j, i))
        elif l[i][j] == -1:
            allTomatoes -= 1
if len(tomatoes) == allTomatoes:
    print(0)
    sys.exit(0)
visited = [[False] * n for _ in range(m)]
print(bfs())