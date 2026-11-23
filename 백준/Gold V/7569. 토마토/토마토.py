import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def isInside(x, y, z): return 0 <= x < a and 0 <= z < b and 0 <= y < c
def bfs():
    global allTomatoes
    q = deque([])
    tomatoes = 0
    for i in range(c):
        for j in range(b):
            for k in range(a):
                if farm[i][j][k] == 1:
                    visited[i][j][k] = 1
                    q.append([k, i, j, 0]) # [x, y, z, distance]
                    tomatoes += 1
                elif farm[i][j][k] == -1:
                    allTomatoes -= 1
    if tomatoes == allTomatoes: return 0
    while q:
        v = q.popleft()
        x, y, z, dist = v
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if not isInside(nx, ny, nz) or visited[ny][nz][nx] or farm[ny][nz][nx] == -1: continue
            q.append([nx, ny, nz, dist+1])
            visited[ny][nz][nx] = 1
            tomatoes += 1
        if tomatoes == allTomatoes: return dist+1
    return -1

a, b, c = map(int, input().split())
farm = [[list(map(int, input().split())) for _ in range(b)] for _ in range(c)] # farm[y][z][x]
visited = [[[0] * a for _ in range(b)] for _ in range(c)] # visited[y][z][x]
allTomatoes = a * b * c
print(bfs())