import sys
from collections import deque

input = sys.stdin.readline

def isInside(x, y): return (0 <= x < m) and (0 <= y < n)

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs(graph, y, x, visited):
    q = deque([(x, y)])
    visited[y][x] = 0
    while q:
        a, b = q.popleft()
        for tu in moves:
            nx, ny = a+tu[1], b+tu[0]
            if not isInside(nx, ny): continue
            if visited[ny][nx] == -1 and graph[ny][nx] != 0:
                q.append((nx, ny))
                visited[ny][nx] = visited[b][a] + 1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
flag = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: bfs(graph, i, j, visited)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited[i][j] = 0
        print(visited[i][j], end = ' ')
    print()