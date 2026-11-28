import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < m
def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and arr[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

for i in range(int(input())):
    print(f"Case #{i+1}: ")
    n, m = map(int, input().split())
    arr = [list(map(int, input().rstrip())) for _ in range(n)]
    for _ in range(int(input())):
        op, *q = input().rstrip().split()
        q = list(map(int, q))
        if op == 'Q':
            ans = 0
            visited = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == 1 and not visited[i][j]:
                        dfs(i, j)
                        ans += 1
            print(ans)
        else:
            arr[q[0]][q[1]] = q[2]