import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 0<=x<n and 0<=y<n
def dfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and not visited[ny][nx] and heights[mi] <= height[ny][nx] <= heights[ma]:
            dfs(nx, ny)

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]
heights = set()
for i in height:
    for j in i:
        heights.add(j)
heights = list(heights)
heights.sort()
mi, ma = 0, 0
ret = 987654321
while ma < len(heights):
    visited = [[0] * n for _ in range(n)]
    if mi > ma or not (heights[mi] <= height[0][0] <= heights[ma]):
        ma += 1
        continue
    dfs(0, 0)
    if not visited[-1][-1]:
        ma += 1
    else:
        ret = min(ret, heights[ma]-heights[mi])
        mi += 1
print(ret)