import sys
from collections import deque
input = sys.stdin.readline

INF = 10**20
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < m
def bfs(s):
    q = deque()
    dist = [[INF for _ in range(m)] for _ in range(n)]
    if s == [-1, -1]:
        for i in range(n):
            if prison[i][0] == '#': q.append([[i, 0], 1])
            elif prison[i][0] != '*': q.appendleft([[i, 0], 0])
        for i in range(n):
            if prison[i][-1] == '#': q.append([[i, m-1], 1])
            elif prison[i][-1] != '*': q.appendleft([[i, m-1], 0])
        for i in range(1, m-1):
            if prison[0][i] == '#': q.append([[0, i], 1])
            elif prison[0][i] != '*': q.appendleft([[0, i], 0])
        for i in range(1, m-1):
            if prison[-1][i] == '#': q.append([[n-1, i], 1])
            elif prison[-1][i] != '*': q.appendleft([[n-1, i], 0])
    else:
        q = deque([[s, 0]])
    for i in q:
        dist[i[0][0]][i[0][1]] = i[1]
    while q:
        p, d = q.popleft()
        x, y = p
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny):
                if prison[nx][ny] == '#' and dist[nx][ny] > d+1:
                    dist[nx][ny] = d+1
                    q.append([[nx, ny], d+1])
                elif prison[nx][ny] in (".", "$") and dist[nx][ny] > d:
                    dist[nx][ny] = d
                    q.appendleft([[nx, ny], d])
    return dist

for _ in range(int(input())):
    n, m = map(int, input().split())
    prison = [list(input().rstrip()) for _ in range(n)]
    starts = [[-1, -1], [-1, -1]]
    for i in range(n):
        for j in range(m):
            if prison[i][j] == '$':
                if starts[0] == [-1, -1]:
                    starts[0] = [i, j]
                else:
                    starts[1] = [i, j]
    dist1 = bfs(starts[0])
    dist2 = bfs(starts[1])
    dist3 = bfs([-1, -1])
    ret = INF
    for i in range(n):
        for j in range(m):
            if INF in [dist1[i][j], dist2[i][j], dist3[i][j]]: continue
            if prison[i][j] == '#':
                ret = min(ret, dist1[i][j] + dist2[i][j] + dist3[i][j] - 2)
            elif prison[i][j] != "*":
                ret = min(ret, dist1[i][j] + dist2[i][j] + dist3[i][j])
    print(min(ret, dist3[starts[0][0]][starts[0][1]] + dist3[starts[1][0]][starts[1][1]]))