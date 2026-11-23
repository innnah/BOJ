import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    q = deque([(a, 0, 0)])
    visited[a] = 1
    while q:
        v = q.popleft()
        if v[0] == b: return v[1], v[2]
        for i, d in graph[v[0]]:
            if not visited[i]:
                q.append((i, v[1]+d, max(d, v[2])))
                visited[i] = 1
    raise ZeroDivisionError("프로그램 좀 잘 짜봐 이 녀석아")

n, r1, r2 = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
ret = bfs(r1, r2)
print(ret[0]-ret[1])