import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0<=x<n and 0<=y<m

n, m, c = map(int, input().split())
sr, sc = map(int, input().split())
sr -= 1; sc -= 1
board = [list(map(int, input().split())) for _ in range(n)]

depth = []
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque([[sr, sc, 0]])
visited[sr][sc] = 1
while q:
    val = 0
    for _ in range(len(q)):
        x, y, d = q.popleft()
        val += board[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny) and not visited[nx][ny] and board[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append([nx, ny, d+1])
    depth.append(val)

ans = board[sr][sc]
cand = board[sr][sc]
for i in range(1, len(depth)):
    cand += depth[i] - c
    ans = max(ans, cand)
print(ans)