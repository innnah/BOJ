import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
d = [False for _ in range(26)]
def isRange(x, y):
    return 0 <= x < c and 0 <= y < r
def toIdx(s):
    return ord(s)-65
def dfs(x, y):
    ret = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isRange(nx, ny) and not d[toIdx(graph[ny][nx])]:
            d[toIdx(graph[ny][nx])] = True
            ret = max(ret, dfs(nx, ny)+1)
            d[toIdx(graph[ny][nx])] = False
    return ret
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
d[toIdx(graph[0][0])] = True
ret = dfs(0, 0)
print(ret)