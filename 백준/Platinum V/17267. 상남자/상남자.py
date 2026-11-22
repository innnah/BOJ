import sys
from collections import deque
input = sys.stdin.readline

def isInside(x, y): return 0<=x<n and 0<=y<m
def bfs():
    q = deque([[start.copy(), a, b]])
    visited[start[0]][start[1]] = 1
    while q:
        v, l, r = q.popleft()
        x, y = v
        if isInside(x+1, y) and not visited[x+1][y] and board[x+1][y] != 1:
            q.appendleft([[x+1, y], l, r])
            visited[x+1][y] = 1
        if isInside(x-1, y) and not visited[x-1][y] and board[x-1][y] != 1:
            q.appendleft([[x-1, y], l, r])
            visited[x-1][y] = 1
        if isInside(x, y+1) and not visited[x][y+1] and board[x][y+1] != 1 and r > 0:
            q.appendleft([[x, y+1], l, r-1])
            visited[x][y+1] = 1
        if isInside(x, y-1) and not visited[x][y-1] and board[x][y-1] != 1 and l > 0:
            q.append([[x, y-1], l-1, r])
            visited[x][y-1] = 1

def bfs2():
    q = deque([[start.copy(), a, b]])
    visited[start[0]][start[1]] = 1
    while q:
        v, l, r = q.popleft()
        x, y = v
        if isInside(x+1, y) and not visited[x+1][y] and board[x+1][y] != 1:
            q.appendleft([[x+1, y], l, r])
            visited[x+1][y] = 1
        if isInside(x-1, y) and not visited[x-1][y] and board[x-1][y] != 1:
            q.appendleft([[x-1, y], l, r])
            visited[x-1][y] = 1
        if isInside(x, y+1) and not visited[x][y+1] and board[x][y+1] != 1 and r > 0:
            q.append([[x, y+1], l, r-1])
            visited[x][y+1] = 1
        if isInside(x, y-1) and not visited[x][y-1] and board[x][y-1] != 1 and l > 0:
            q.appendleft([[x, y-1], l-1, r])
            visited[x][y-1] = 1

n, m = map(int, input().split())
a, b = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
start = [-1, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start = [i, j]
visited = [[0 for _ in range(m)] for _ in range(n)]
bfs()
res = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        res[i][j] = visited[i][j]
visited = [[0 for _ in range(m)] for _ in range(n)]
bfs2()
for i in range(n):
    for j in range(m):
        res[i][j] = visited[i][j] or res[i][j]
print(sum([res[i].count(1) for i in range(n)]))