import sys
input = sys.stdin.readline
n, m = map(int, input().split())
y, x, d = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 0
while True:
    if not l[y][x]:
        l[y][x] = 2
        cnt += 1
    for i in range(4):
        d = (d+3)%4
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < m and 0 <= ny < n and not l[ny][nx]:
            x, y = nx, ny
            break
    else:
        nx, ny = x - dx[d], y - dy[d]
        if l[ny][nx] != 1:
            x, y = nx, ny
        else:
            break
print(cnt)