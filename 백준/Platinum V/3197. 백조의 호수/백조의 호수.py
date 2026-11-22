import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def isInside(x, y): return 0<=x<n and 0<=y<m

def find(x, y):
    if unionfind[x][y] == (x, y): return (x, y)
    unionfind[x][y] = find(*unionfind[x][y])
    return unionfind[x][y]

def union(r1, r2):
    unionfind[r2[0]][r2[1]] = r1
    size[r1[0]][r1[1]] += size[r2[0]][r2[1]]
    size[r2[0]][r2[1]] = 0

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
unionfind = [[(i, j) for j in range(m)] for i in range(n)]
size = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            size[i][j] += 1
            cnt += 1

q = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
discovered = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X': continue
        r = find(i, j)
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if isInside(nx, ny):
                if arr[nx][ny] != "X":
                    r2 = find(nx, ny)
                    if r != r2:
                        union(r, r2)
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

day = 1
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        discovered[x][y] = 1
        r = find(x, y)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny):
                if arr[nx][ny] != 'X' or discovered[nx][ny]:
                    r2 = find(nx, ny)
                    if r2 != r:
                        union(r, r2)
                    if size[r[0]][r[1]] == cnt:
                        print(day)
                        sys.exit(0)
                elif arr[nx][ny] == 'X' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    day += 1