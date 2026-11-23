import sys
input = sys.stdin.readline

d = {'D': (0, 1), 'U': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
def bfs(start, num):
    global ret
    x, y = start
    visited[y][x] = num
    while True:
        nx, ny = x + d[dirMap[y][x]][0], y + d[dirMap[y][x]][1]
        if visited[ny][nx] == num:
            ret += 1
            return
        elif visited[ny][nx] not in (0, num):
            return
        visited[ny][nx] = num
        x, y = nx, ny

n, m = map(int, input().split())
dirMap = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
ret = 0
cnt = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs((j, i), cnt)
            cnt += 1
print(ret)