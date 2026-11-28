import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n)]
nxt = [0 for _ in range(m+1)]
for i in range(n-1, -1, -1):
    a, b = edges[i]
    nxt[b] = a
visited = [0 for _ in range(m+1)]
visited[p] = 1
ret = 0
cur = p
while 1:
    if nxt[cur] == 0:
        print(ret)
        break
    if visited[nxt[cur]] == 1:
        print(-1)
        break
    visited[nxt[cur]] = 1
    cur = nxt[cur]
    ret += 1