import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def isInside(x, y): return 0 < x <= n and 0 < y <= n
def bfs(x, y):
    visited[y][x] = 1
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if isInside(nx, ny) and not visited[ny][nx] and not (((cx, cy), (nx, ny)) in s):
                q.append((nx, ny))
                visited[ny][nx] = 1

n, k, r = map(int, input().split())
s = set()
for _ in range(r):
    a, b, c, d = map(int, input().split())
    s.add(((a, b), (c, d)))
    s.add(((c, d), (a, b)))
cows = [tuple(map(int, input().split())) for _ in range(k)]
ret = 0
for x, y in cows:
    visited = [[0] * (n+1) for _ in range(n+1)]
    bfs(x, y)
    for cow in cows:
        if not visited[cow[1]][cow[0]]:
            ret += 1
print(ret//2)