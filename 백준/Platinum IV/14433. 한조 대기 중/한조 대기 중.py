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
n, m, k1, k2 = map(int, input().split())
d = [0 for _ in range(m+1)]
match = [[] for _ in range(n+1)]
for _ in range(k1):
    a, b = list(map(int, input().split()))
    match[a].append(b)
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)
ret1 = m+1-d.count(0)
d = [0 for _ in range(m+1)]
match = [[] for _ in range(n+1)]
for _ in range(k2):
    a, b = list(map(int, input().split()))
    match[a].append(b)
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)
ret2 = m+1-d.count(0)
if ret1 >= ret2:
    print("그만 알아보자")
else:
    print("네 다음 힐딱이")