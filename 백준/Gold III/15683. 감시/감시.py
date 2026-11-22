import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = [[], [0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            cctv.append((i, j, board[i][j]))

ans = 10**9
for i in range(4**len(cctv)):
    nboard = [row[:] for row in board]
    bi = bin(i)[2:].zfill(len(cctv)*2)
    for j in range(len(cctv)):
        d = int(bi[j*2:j*2+2], 2)
        x, y, t = cctv[j]
        for k in dir[t]:
            nd = (k + d) % 4
            nx, ny = x, y
            while True:
                nx += dx[nd]
                ny += dy[nd]
                if 0 <= nx < n and 0 <= ny < m and nboard[nx][ny] != 6:
                    if nboard[nx][ny] == 0:
                        nboard[nx][ny] = t
                else:
                    break
    cnt = sum(row.count(0) for row in nboard)
    ans = min(ans, cnt)
print(ans)