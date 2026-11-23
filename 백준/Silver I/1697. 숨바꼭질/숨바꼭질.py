import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(n, 0)])
    visited[n] = 1
    while q:
        v, dist = q.popleft()
        if v == m: return dist
        if v <= m and not visited[v*2]:
            visited[v*2] = 1
            q.append((v*2, dist+1))
        if v+1 <= m*2 and not visited[v+1]:
            visited[v+1] = 1
            q.append((v+1, dist+1))
        if v-1 >= 0 and not visited[v-1]:
            visited[v-1] = 1
            q.append((v-1, dist+1))
    return "___oops___"

n, m = map(int, input().split())
visited = [0 for _ in range(max(n, m)*2+1)]
print(bfs())