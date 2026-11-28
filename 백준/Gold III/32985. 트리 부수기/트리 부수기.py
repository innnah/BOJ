import sys
sys.setrecursionlimit(200127)
input = sys.stdin.readline

def dfs(v, d):
    depth[v] = d
    for i in graph[v]:
        if not depth[i]:
            dfs(i, d+1)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
depth = [0 for _ in range(n)]
dfs(0, 1)
ans = 0
for i in range(n-1, 0, -1):
    print((n - depth[i]) % 2, end = '')