import sys
input = sys.stdin.readline

def dfs(v):
    if visited[v]: return 0
    visited[v] = 1
    for i in match[v]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = v
            return 1
    return 0
n, m = map(int, input().split())
d = [0 for _ in range(m+1)]
match = [[]]
for _ in range(n):
    _, *a = list(map(int, input().split()))
    match.append(a)
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)
print(m+1-d.count(0))