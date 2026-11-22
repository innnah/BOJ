import sys
sys.setrecursionlimit(115000)
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
    for i in range(n):
        if discovered[i] == -1: scc(i)
    ids = [[] for _ in range(n)]
    for i in range(n):
        ids[sccId[i]].append(i)
    for i in range(n):
        ids[i].sort()
    return ids

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
discovered = [-1 for _ in range(n)]
sccId = [-1 for _ in range(n)]
stack = []
sccCounter, vertexCounter = 0, 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
ret = tarjanSCC()
scc_indegree = [0 for _ in range(max(sccId)+1)]
for i in range(n):
    for j in graph[i]:
        if sccId[i] != sccId[j]:
            scc_indegree[sccId[j]] += 1
print(scc_indegree.count(0))