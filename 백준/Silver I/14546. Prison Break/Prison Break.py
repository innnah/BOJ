import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(r, c): return 0 <= r < n and 0 <= c < m
def dfs(r, c):
    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if isInside(nr, nc) and not visited[nr][nc] and board[r][c] == board[nr][nc]:
            dfs(nr, nc)

for _ in range(int(input())):
    m, n, c1, r1, c2, r2 = map(int, input().split())
    c1 -= 1; c2 -= 1; r1 = n-r1; r2 = n-r2
    board = [list(input().rstrip()) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dfs(r1, c1)
    print("YES" if visited[r2][c2] else "NO")