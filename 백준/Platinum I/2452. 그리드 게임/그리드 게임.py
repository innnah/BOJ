import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0<=x<m and 0<=y<n
def dfs(x, y, k):
    visited[y][x] = k
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny):
            if not visited[ny][nx] and arr[ny][nx] == arr[y][x]:
                dfs(nx, ny, k)
def dfs2(x, y):
    visited2[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny):
            if not visited2[ny][nx] and visited[ny][nx] == visited[y][x]:
                dfs2(nx, ny)
            elif visited[ny][nx] != visited[y][x]:
                graph[visited[y][x]].append(visited[ny][nx])
                graph[visited[ny][nx]].append(visited[y][x])
def bfs(s):
    q = deque([(s, 0)])
    visited[s] = 1
    while q:
        node, dist = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append((i, dist+1))
                visited[i] = 1
                depth[i] = dist+1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
k = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            k += 1
            dfs(j, i, k)
visited2 = [[0 for _ in range(m)] for _ in range(n)]
graph = [[] for _ in range(k+1)]
for i in range(n):
    for j in range(m):
        if not visited2[i][j]:
            dfs2(j, i)
for i in range(1, k+1):
    graph[i] = list(set(graph[i]))
ret = 987654321
mini = [0 for _ in range(k+1)]
for i in range(1, k+1):
    if mini[i] >= ret: continue
    depth = [0 for _ in range(k+1)]
    visited = [0 for _ in range(k+1)]
    bfs(i)
    cand = 0
    for i in range(1, k+1):
        mini[i] = max(mini[i], depth[i])
        cand = max(cand, depth[i])
    ret = min(ret, cand)
print(ret)