import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(v, cur):
    global maxDist, maxNode
    visited[v] = 1
    dist = 0
    for node, cost in graph[v]:
        if not visited[node]:
            dist = max(dfs(node, cur+cost) + cost, dist)
    if dist == 0 and cur >= maxDist:
        maxDist = cur
        maxNode = v 
    return dist

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
maxNode, maxDist = 0, 0
for _ in range(n):
    v, *l, _ = list(map(int, input().split()))
    for i in range(0, len(l), 2):
        graph[v].append((l[i], l[i+1]))
        graph[l[i]].append((v, l[i+1]))
dfs(2, 0)
visited = [0 for _ in range(n+1)]
print(dfs(maxNode, 0))