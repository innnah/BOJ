import sys
from collections import deque
input = sys.stdin.readline

n, o, s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n*o+1)]
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(o):
        graph[n*i + a].append(n*i + b)
        graph[n*i + b].append(n*i + a)
p = int(input())
for _ in range(p):
    a, b = map(int, input().split())
    graph[n*(a-1)+b].append(n*a+b)

dist = -1
q = deque([(s,0)])
visited = [0 for _ in range(n*o+1)]
visited[s] = 1
while q:
    v, d = q.popleft()
    if v == e+n*(o-1):
        dist = d
        break
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            q.append((i, d+1))

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if dist != -1:
        print((o-1)*b+(dist-o+1)*a)
    else:
        print(-1)