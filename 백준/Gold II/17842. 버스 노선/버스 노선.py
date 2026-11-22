import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(n):
    if len(graph[i]) == 1:
        cnt += 1
print((cnt+1)//2)