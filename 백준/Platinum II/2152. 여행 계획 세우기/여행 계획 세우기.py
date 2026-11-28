import sys
sys.setrecursionlimit(110000)
input = sys.stdin.readline

def scc(v):
    global vertexCounter, sccCounter
    discovered[v] = vertexCounter
    vertexCounter += 1
    ret = discovered[v]
    stack.append(v)
    for i in graph[v]:
        if discovered[i] == -1:
            ret = min(ret, scc(i))
        elif sccId[i] == -1:
            ret = min(ret, discovered[i])
    if ret == discovered[v]:
        while 1:
            t = stack.pop()
            sccId[t] = sccCounter
            if t == v: break
        sccCounter += 1
    return ret
def tarjanSCC():
    global sccCounter, vertexCounter
    for i in range(1, n+1):
        if discovered[i] == -1: scc(i)
def genGraph(v):
    visited[v] = 1
    for i in graph[v]:
        if sccId[i] != sccId[v]:
            sccGraph[sccId[v]].append(sccId[i])
        if not visited[i]:
            genGraph(i)
def dfs(v):
    if v == e:
        return 0
    if dp[v] != -1: return dp[v]
    for i in sccGraph[v]:
        cand = dfs(i)
        if cand != -1:
            dp[v] = max(dp[v], cand+sccLen[i])
    return dp[v]

n, m, s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
discovered = [-1 for _ in range(n+1)]
sccId = [-1 for _ in range(n+1)]
stack = []
sccCounter, vertexCounter = 0, 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
tarjanSCC()
sccLen = [0 for _ in range(n+1)]
for i in range(1, n+1):
    sccLen[sccId[i]] += 1
visited = [0 for _ in range(n+1)]
sccGraph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    if not visited[i]: genGraph(i)
s, e = sccId[s], sccId[e]
dp = [-1 for _ in range(n+1)]
ret = dfs(s)
if ret != -1:
    print(ret+sccLen[s])
else:
    print(0)