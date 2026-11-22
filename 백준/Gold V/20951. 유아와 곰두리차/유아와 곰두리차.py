import sys
sys.setrecursionlimit(700127)
input = sys.stdin.readline

def dfs(v, depth):
    if depth == 7: return 1
    for i in graph[v]:
        if visited[i][depth+1] == 0:
            visited[v][depth] += dfs(i, depth+1)
        else:
            visited[v][depth] += visited[i][depth+1]
        visited[v][depth] %= 10**9 + 7
    return visited[v][depth]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [[0 for _ in range(8)] for _ in range(n+1)]
ret = 0
for i in range(1, n+1):
    ret += dfs(i, 0)
    ret %= 10**9 + 7
print(ret)