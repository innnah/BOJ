import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx] and places[ny][nx]:
            dfs(nx, ny)

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    places = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        places[b][a] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and places[i][j]:
                dfs(j, i)
                cnt += 1
    print(cnt)