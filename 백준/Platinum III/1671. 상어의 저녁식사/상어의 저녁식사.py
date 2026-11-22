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

n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
n = len(l)
d = [-1 for _ in range(n)]
match = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            if l[i][0] >= l[j][0] and l[i][1] >= l[j][1] and l[i][2] >= l[j][2]:
                if l[i][0] == l[j][0] and l[i][1] == l[j][1] and l[i][2] == l[j][2]:
                    if i < j:
                        match[i].append(j)
                else:
                    match[i].append(j)
for i in range(n):
    for _ in range(2):
        visited = [0 for _ in range(n)]
        dfs(i)
print(d.count(-1))