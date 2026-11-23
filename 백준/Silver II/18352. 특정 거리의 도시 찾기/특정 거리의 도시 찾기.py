import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([(start, 0)])
    visited[start] = 1
    while q:
        node, dist = q.popleft()
        if dist == k:
            ret.append(node)
            continue
        for ne in graph[node]:
            if not visited[ne]:
                q.append((ne, dist+1))
                visited[ne] = 1

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
ret = []
bfs(x)
ret.sort()
if len(ret):
    for i in ret:
        print(i)
else:
    print(-1)