import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

def dfs(v):
    if visited[v]: return 0
    visited[v] = 1
    for i in match[v]:
        if d[i] == -1 or dfs(d[i]):
            d[i] = v
            return 1
    return 0

n, m, k = map(int, input().split())
pp = []
kk = []
for _ in range(k):
    a, b, c = map(int, input().split())
    if c == 0:
        pp.append((a, b))
    else:
        kk.append((a, b))
match = [[] for _ in range(len(pp))]
for i in range(len(pp)):
    for j in range(len(kk)):
        if pp[i][0] == kk[j][0] or pp[i][1] == kk[j][1]:
            match[i].append(j)

d = [-1 for _ in range(len(kk))]
for i in range(len(pp)):
    visited = [0 for _ in range(len(pp))]
    dfs(i)
print(len(kk) - d.count(-1))