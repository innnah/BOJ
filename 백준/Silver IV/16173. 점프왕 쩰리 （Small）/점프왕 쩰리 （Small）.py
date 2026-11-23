import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < n
def bfs():
    q = deque([[0, 0]])
    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        if jumpMap[y][x] == -1: return "HaruHaru"
        for i in range(4):
            nx, ny = x + dx[i] * jumpMap[y][x], y + dy[i] * jumpMap[y][x]
            if not isInside(nx, ny) or visited[ny][nx]: continue
            q.append([nx, ny])
            visited[ny][nx] = True
    return "Hing"

n = int(input())
jumpMap = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited[0][0] = True
print(bfs())