import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
d = {"L" : 0, "R" : 1, "U" : 2, "D" : 3, "-" : -1}
rd = ["R", "L", "D", "U"]
def isInside(x, y): return 0 <= x < n and 0 <= y < n
def nxt(x, y, dir): return isInside(x, y) and not usable[x][y] and (board[x][y] == '-' or board[x][y] == dir)
def dfs(x, y):
    global newans
    if usable[x][y]: return
    usable[x][y] = 1
    newans -= 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and not usable[nx][ny] and (board[nx][ny] == '-' or d[rd[d[board[nx][ny]]]] == i):
            dfs(nx, ny)

n, m = map(int, input().split())
querys = []
for _ in range(m):
    a, b, c = input().rstrip().split()
    querys.append([int(a)-1, int(b)-1, c])

board = [['-' for _ in range(n)] for _ in range(n)]
for x, y, dir in querys:
    board[x][y] = dir

usable = [[0 for _ in range(n)] for _ in range(n)]
newans = n*n
for i in range(n):
    if nxt(0, i, 'U'):
        dfs(0, i)
    if nxt(n-1, i, 'D'):
        dfs(n-1, i)
    if nxt(i, 0, 'L'):
        dfs(i, 0)
    if nxt(i, n-1, 'R'):
        dfs(i, n-1)

ans = [0 for _ in range(m)]
ans[m-1] = newans
for i in range(m-2, -1, -1):
    x, y, dir = querys[i+1]
    newans = ans[i+1]
    board[x][y] = '-'
    for j in range(4):
        nx, ny = x + dx[j], y + dy[j]
        if not isInside(nx, ny) or usable[nx][ny]:
            dfs(x, y)
            break
    ans[i] = newans
for i in range(m):
    print(ans[i])