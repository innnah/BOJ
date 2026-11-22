import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def isInside(r, c): return 0 <= r < n and 0 <= c < m
def dfs(r, c):
    visited[r][c] = len(blocks) - 1
    blocks[-1].append([r, c])
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if isInside(nr, nc) and arr[nr][nc] == arr[r][c] and visited[nr][nc] == -1:
            dfs(nr, nc)

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
blocks = []
visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and arr[i][j] != "X":
            blocks.append([])
            dfs(i, j)
ne = [[[-1, -1] for _ in range(8)] for _ in range(len(blocks))]
for i in range(len(blocks)):
    for dp in range(4):
        for cc in range(-1, 2, 2):
            abs_cc = (dp+cc)%4
            if dr[dp] == 0:
                blocks[i].sort(key = lambda x : [dc[dp] * -x[1], dr[abs_cc] * -x[0]])
            else:
                blocks[i].sort(key = lambda x : [dr[dp] * -x[0], dc[abs_cc] * -x[1]])
            tmp = blocks[i][0].copy()
            tmp[0] += dr[dp]
            tmp[1] += dc[dp]
            ne[i][dp*2+(cc+1)//2] = tmp.copy()
dp = 0
cc = -1
cur = 0
while True:
    transform = blocks[cur][0]
    print(arr[transform[0]][transform[1]], end = '')
    cnt = 0
    while cnt < 8:
        tmp = ne[cur][dp*2+(cc+1)//2].copy()
        if isInside(*tmp) and arr[tmp[0]][tmp[1]] != 'X': break
        if cnt % 2:
            dp = (dp+1)%4
        else:
            cc = -cc
        cnt += 1
    if cnt == 8: break
    tmp = ne[cur][dp*2+(cc+1)//2].copy()
    cur = visited[tmp[0]][tmp[1]]