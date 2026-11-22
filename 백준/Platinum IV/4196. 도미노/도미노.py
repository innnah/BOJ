import sys
sys.setrecursionlimit(130000)
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
    ids = [[] for _ in range(n)]
    for i in range(1, n+1):
        ids[sccId[i]].append(i)
    return ids
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    discovered = [-1 for _ in range(n+1)]
    sccId = [-1 for _ in range(n+1)]
    stack = []
    sccCounter, vertexCounter = 0, 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    sccs = tarjanSCC()
    #print(sccs)
    ret = 0
    sccGraph = [set() for _ in range(len(sccs))]
    indegree = [0 for _ in range(len(sccs))]
    for i in range(1, n+1):
        for j in graph[i]:
            if sccId[i] != sccId[j]:
                sccGraph[sccId[i]].add(sccId[j])
                indegree[sccId[j]] += 1
    #print(sccGraph)
    for i in range(len(sccs)):
        if indegree[i] == 0 and sccs[i]:
            ret += 1
    print(ret)