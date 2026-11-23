import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]
def dfs(x,y):
    v[y][x] = 1
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny< m and not v[ny][nx] and p[ny][nx]:
            dfs(nx, ny)
while 1:
    n,m = map(int,input().split())
    if n==0 and m==0: break
    p = [list(map(int, input().split())) for _ in range(m)]
    v = [[0] * n for _ in range(m)]
    c = 0
    for i in range(m):
        for j in range(n):
            if not v[i][j] and p[i][j]:
                dfs(j,i)
                c+=1
    print(c)