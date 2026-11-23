import sys
from collections import deque
input = sys.stdin.readline

INF = 987654321
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < n
def bfs(start, fish, size):
    q = deque([[start, 0]])
    visited = [[0] * n for _ in range(n)]
    visited[start[1]][start[0]] = 1
    while q:
        v = q.popleft()
        xy, time = v
        if xy == fish: return time
        x, y = xy
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not isInside(nx, ny) or visited[ny][nx] or (m[ny][nx] > size and m[ny][nx] != 9): continue
            visited[ny][nx] = 1
            q.append([(nx, ny), time+1])
    return INF
def main(start):
    cnt = 0
    size = 2
    time = 0
    x, y = start
    while fishes:
        minimum = INF
        minIdx = -1
        for i in range(len(fishes)):
            if m[fishes[i][1]][fishes[i][0]] < size:
                v = bfs((x, y), fishes[i], size)
                if v < minimum:
                    minimum = v
                    minIdx = i
        if minimum == INF: return time
        time += minimum
        x, y = fishes[minIdx]
        cnt += 1
        del fishes[minIdx]

        if cnt == size:
            size += 1
            cnt = 0
    return time

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
fishes = []
start = (-1, -1)
for i in range(n):
    for j in range(n):
        if m[i][j] == 9:
            start = (j, i)
        elif m[i][j] != 0:
            fishes.append((j, i))
print(main(start))