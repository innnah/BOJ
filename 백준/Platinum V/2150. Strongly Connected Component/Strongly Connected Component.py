import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

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
    ret = []
    for i in range(1, n+1):
        ids[sccId[i]].append(i)
    for i in range(n):
        if len(ids[i]) != 0:
            ids[i].sort()
            ret.append(ids[i])
    return ret

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
discovered = [-1 for _ in range(n+1)]
sccId = [-1 for _ in range(n+1)]
stack = []
sccCounter, vertexCounter = 0, 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
ret = tarjanSCC()
print(len(ret))
ret.sort()
for i in ret:
    print(*i, -1)