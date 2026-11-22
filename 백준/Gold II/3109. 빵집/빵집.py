import sys
input = sys.stdin.readline

def dfs(r, c):
    visited[r][c] = 1
    if c == m-1:
        return 1
    v = 0
    if r > 0 and not visited[r-1][c+1]:
        v = dfs(r-1, c+1)
    if not v and not visited[r][c+1]:
        v = dfs(r, c+1)
    if not v and r < n-1 and not visited[r+1][c+1]:
        v = dfs(r+1, c+1)
    return v

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = arr[i][j] == 'x'
cnt = 0
for i in range(n):
    if not visited[i][0]:
        cnt += dfs(i, 0)
print(cnt)