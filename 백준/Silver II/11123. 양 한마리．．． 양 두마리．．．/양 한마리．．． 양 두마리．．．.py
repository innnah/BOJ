import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def isInside(x, y): return (0 <= x < a) and (0 <= y < b)
def dfs(x, y, visited):
    if not isInside(x, y): return
    visited[x][y] = '.'
    if isInside(x+1, y) and visited[x+1][y] == '#': dfs(x+1, y, visited)
    if isInside(x-1, y) and visited[x-1][y] == '#': dfs(x-1, y, visited)
    if isInside(x, y+1) and visited[x][y+1] == '#': dfs(x, y+1, visited)
    if isInside(x, y-1) and visited[x][y-1] == '#': dfs(x, y-1, visited)

for _ in range(int(input())):
    a, b = map(int, input().split())
    visited = [list(input()) for _ in range(a)]
    cnt = 0
    for i in range(a):
        for j in range(b):
            if visited[i][j] == '#':
                dfs(i, j, visited)
                cnt += 1
    print(cnt)