import sys
sys.setrecursionlimit(127127)
input = sys.stdin.readline

def dfs1(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs1(i)
    stack.append(v)
def dfs2(v):
    visited[v] = 1
    sccId[v] = cnt
    for i in rgraph[v]:
        if not visited[i]:
            dfs2(i)

n, m = map(int, input().split())
graph = [[] for _ in range(2*n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)

sccId = [-1 for _ in range(2*n+1)]
stack = []
visited = [0 for _ in range(2*n+1)]
for i in range(-n, n+1):
    if i == 0:
        continue
    if not visited[i]:
        dfs1(i)

rgraph = [[] for _ in range(2*n+1)]
for i in range(-n, n+1):
    if i == 0:
        continue
    for j in graph[i]:
        rgraph[j].append(i)

visited = [0 for _ in range(2*n+1)]
cnt = 0
while stack:
    v = stack.pop()
    if not visited[v]:
        cnt += 1
        dfs2(v)

for i in range(1, n+1):
    if sccId[i] == sccId[-i]:
        print(0)
        break
else:
    print(1)