import sys
sys.setrecursionlimit(271127)
input = sys.stdin.readline

def dfs1(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs1(i)
    stack.append(v)
def dfs2(v):
    visited[v] = 1
    scc[-1].append(v)
    for i in rgraph[v]:
        if not visited[i]:
            dfs2(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
rgraph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    rgraph[b].append(a)
visited = [0 for _ in range(n+1)]
stack = []
for i in range(1, n+1):
    if not visited[i]:
        dfs1(i)
visited = [0 for _ in range(n+1)]
scc = []
for _ in range(len(stack)):
    v = stack.pop()
    if not visited[v]:
        scc.append([])
        dfs2(v)
if len(scc) == 1:
    print("Yes")
else:
    print("No")