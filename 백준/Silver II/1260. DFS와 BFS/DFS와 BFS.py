from collections import deque
import sys

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [False] * (n+1)
dfs(graph, s, visited)
print()
visited = [False] * (n+1)
bfs(graph, s, visited)