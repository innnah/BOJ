import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([[1, 1]])
    while q:
        num, mod = q.popleft()
        nv0 = [num*10, (mod*10)%n]
        nv1 = [num*10+1, (mod*10+1)%n]
        if not visited[nv0[1]]:
            visited[nv0[1]] = nv0[0]
            q.append(nv0)
        if not visited[nv1[1]]:
            visited[nv1[1]] = nv1[0]
            q.append(nv1)

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    visited = [0 for _ in range(n)]
    visited[1] = 1
    bfs()
    if visited[0] == 0:
        print("BRAK")
    else:
        print(visited[0])