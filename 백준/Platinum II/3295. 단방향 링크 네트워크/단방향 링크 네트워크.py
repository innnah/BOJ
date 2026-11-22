import sys
input = sys.stdin.readline

def dfs(v):
    if visited[v]: return 0
    visited[v] = 1
    for i in match[v]:
        if d[i] == -1 or dfs(d[i]):
            d[i] = v
            return 1
    return 0

for _ in range(int(input())):
    n, m = map(int, input().split())
    match = [[] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        match[a].append(b)
    d = [-1 for _ in range(n)]
    for i in range(n):
        visited = [0 for _ in range(n)]
        dfs(i)
    print(n - d.count(-1))