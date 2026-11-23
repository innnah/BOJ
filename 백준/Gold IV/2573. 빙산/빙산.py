import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def melt():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j]:
                for k in range(4):
                    nx, ny = j + dx[k], i + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and l[ny][nx] == 0: 
                        tmp[i][j] += 1
    for i in range(n):
        for j in range(m):
            l[i][j] -= min(tmp[i][j], l[i][j])
def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and l[ny][nx]:
                visited[ny][nx] = 1
                q.append((nx, ny))

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    flag = False
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and l[i][j]:
                if flag:
                    print(cnt)
                    sys.exit(0)
                bfs(j, i)
                flag = True
    else:
        flag = False
        for i in range(n):
            for j in range(m):
                if l[i][j]: flag = True
        if not flag:
            print(0)
            sys.exit(0)
    melt()
    cnt += 1