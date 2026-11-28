import sys
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth+1)
        else:
            if i == start:
                roots.append(start)
                cyc.append(depth)
def dfs2(v):
    visited[v] = 1
    nodes = 1
    for i in graph[v]:
        if not visited[i]:
            nodes += dfs2(i)
    return nodes

n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(n):
    graph[arr[i]].append(i+1)
visited = [0 for _ in range(n+1)]
roots = []
cyc = []
for i in range(1, n+1):
    if not visited[i]:
        start = i
        dfs(i, 1)

visited = [0 for _ in range(n+1)]
size = []
for i in roots:
    size.append(dfs2(i))

dp = [0 for _ in range(m+1)]
dp[0] = 1
for i in range(len(roots)):
    dp2 = dp.copy()
    for j in range(cyc[i], size[i]+1):
        for k in range(m, -1, -1):
            if k - j >= 0:
                dp2[k] |= dp[k-j]
            else:
                break
    dp = dp2.copy()
for i in range(m, -1, -1):
    if dp[i] == 1:
        print(i)
        break
