import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(0, 0, 1, 0, 0)])
    visited[0][0][0][0] = 1
    while q:
        x, y, day, time, cnt = q.popleft()
        if x == n-1 and y == n-1: return day, ("moon" if time else "sun")
        ntime, ncnt, nday = time, cnt, day
        ncnt += 1
        if ncnt >= m: 
            ntime += 1
            ncnt = 0
        if ntime >= 2: 
            nday += 1
            ntime = 0
        for i in range(4):
            nx, ny = precalc[y][x][i]
            if nx == -1 and ny == -1: continue
            isDay = abs(x-nx) == 1 or abs(y-ny) == 1
            if (isDay or time) and not visited[ny][nx][ntime][ncnt]:
                q.append((nx, ny, nday, ntime, ncnt))
                visited[ny][nx][ntime][ncnt] = 1
    return (-1,)

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
precalc = [[[(-1, -1)] * 4 for _ in range(n)] for _ in range(n)]
visited = [[[[0] * 10 for _ in range(2)] for _ in range(n)] for _ in range(n)]
trace = [[(-1, -1)] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(n):
    for j in range(n):
        for d in range(4):
            x, y = j, i
            nx, ny = x + dx[d], y + dy[d]
            while 0 <= nx < n and 0 <= ny < n and l[ny][nx]:
                nx += dx[d]
                ny += dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                precalc[y][x][d] = (nx, ny)
print(*bfs())