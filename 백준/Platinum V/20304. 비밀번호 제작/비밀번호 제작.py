import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    for i in l:
        q.append((i, 1))
        distance[i] = 1
    while q:
        v, dist = q.popleft()
        a = 1
        while a <= maximum:
            if v&a and not distance[v-a]:
                q.append((v-a, dist+1))
                distance[v-a] = dist+1
            elif not (v&a) and v+a <= maximum and not distance[v+a]:
                q.append((v+a, dist+1))
                distance[v+a] = dist+1
            a *= 2

maximum = int(input())
n = int(input())
l = list(map(int, input().split()))
distance = [0 for _ in range(maximum+1)]
bfs()
print(max(distance)-1)