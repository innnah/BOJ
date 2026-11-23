import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y):
    visited[y][x] = 1
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and places[ny][nx]:
            cnt += dfs(nx, ny) + 1
    return cnt

n = int(input())
places = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0
l = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and places[i][j]:
            l.append(dfs(j, i)+1)
            cnt += 1
l.sort()
print(cnt)
for i in l:
    print(i)