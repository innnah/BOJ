dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0 <= x < 5 and 0 <= y < 5
def dfs(x, y, moved = 0, eaten = 0):
    if eaten >= 2:
        print(1)
        exit(0)
    if moved >= 3:
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and l[ny][nx] != -1 and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(nx, ny, moved+1, eaten+l[ny][nx])
            visited[ny][nx] = 0
l = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())
visited[r][c] = 1
dfs(c,r)
print(0)