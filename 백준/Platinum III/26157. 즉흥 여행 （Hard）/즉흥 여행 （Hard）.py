import sys
sys.setrecursionlimit(200127)
from collections import deque
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
    sccId[v] = len(scc)-1
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
sccId = [-1 for _ in range(n+1)]
while stack:
    st = stack.pop()
    if not visited[st]:
        scc.append([])
        dfs2(st)

sccGraph = [[] for _ in range(len(scc))]
indegree = [0 for _ in range(len(scc))]
for i in range(1, n+1):
    for j in graph[i]:
        if sccId[i] != sccId[j]:
            sccGraph[sccId[i]].append(sccId[j])
            indegree[sccId[j]] += 1

cand = []
for i in range(len(scc)):
    if indegree[i] == 0:
        cand.append(i)

if len(cand) == 1:
    q = deque(cand)
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            for i in sccGraph[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if len(q) >= 2:
            print(0)
            sys.exit(0)
    print(len(scc[cand[0]]))
    scc[cand[0]].sort()
    print(*scc[cand[0]])
else:
    print(0)