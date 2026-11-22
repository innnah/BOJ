import sys
input = sys.stdin.readline
def dfs(v):
    visited[v] = 1
    cnt = 0
    for i in graph[v]:
        if not visited[i]:
            cnt += dfs(i) + 1
    return cnt
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(1))