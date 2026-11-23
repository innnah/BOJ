import sys
input = sys.stdin.readline
sys.setrecursionlimit(300010)

def f(n): return n*(n-1)//2
def dfs(v):
    global ret
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            visited[v] += dfs(i)
    ret += f(n) - f(n-visited[v])
    return visited[v]
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
ret = 0
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(ret - f(n))