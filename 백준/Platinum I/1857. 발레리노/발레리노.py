import sys

from collections import deque

input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, 1, -1, -1]

dy = [1, -1, 1, -1, 2, -2, 2, -2]

def isInside(x, y): return 0<=x<m and 0<=y<n

def dfs(x, y, cx, cy):

    visited[cy][cx] = 1

    if (x, y) != (cx, cy) and arr[cy][cx] != 1:

        graph[y][x].append((cx, cy))

        return

    for i in range(8):

        nx, ny = cx+dx[i], cy+dy[i]

        if isInside(nx, ny) and arr[ny][nx] != 2 and not visited[ny][nx]:

            dfs(x, y, nx, ny)

def bfs():

    q = deque([[start, 1]])

    while q:

        v, d = q.popleft()

        x, y = v

        if arr[y][x] == 4: return d

        for i in graph[y][x]:

            nx, ny = i

            if not dist[ny][nx]:

                q.append([(nx, ny), d+1])

                dist[ny][nx] = d+1

    return -1

def bfs2():

    q = deque([[start, 1]])

    while q:

        v, d = q.popleft()

        x, y = v

        for i in graph[y][x]:

            nx, ny = i

            if not visited[ny][nx]:

                q.append([(nx, ny), d+1])

                visited[ny][nx] = 1

            if d+1 == dist[ny][nx]:

                dp[ny][nx] += dp[y][x]

    

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

graph = [[[] for _ in range(m)] for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dist = [[0] * m for _ in range(n)]

dp = [[0] * m for _ in range(n)]

start = (-1, -1)

end = (-1, -1)

for i in range(n):

    for j in range(m):

        if arr[i][j] not in [1, 2]:

            visited = [[0] * m for _ in range(n)]

            dfs(j, i, j, i)

        if arr[i][j] == 3:

            start = (j, i)

            dist[i][j] = 1

            dp[i][j] = 1

        if arr[i][j] == 4:

            end = (j, i)

ret = bfs()

if ret == -1:

    print(-1)

else:

    print(ret-2)

    visited = [[0] * m for _ in range(n)]

    bfs2()

    print(dp[end[1]][end[0]])