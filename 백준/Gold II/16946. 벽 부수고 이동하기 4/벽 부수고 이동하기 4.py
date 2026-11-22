import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
reachable = [[0 for _ in range(m)] for _ in range(n)]
group = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

no = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            cells = []
            cells.append((i, j))
            visited[i][j] = 1
            q = deque()
            q.append((i, j))
            cnt = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 0:
                        cells.append((nx, ny))
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        cnt += 1
            for x, y in cells:
                reachable[x][y] = cnt
                group[x][y] = no
            no += 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            nos = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and group[nx][ny] not in nos:
                    board[i][j] += reachable[nx][ny]
                    nos.add(group[nx][ny])
            board[i][j] %= 10

for row in board:
    print("".join(map(str, row)))
