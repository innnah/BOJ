import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)
def solve(v):
    visited[v] = 1
    ret = 1
    for i in graph[v]:
        if not visited[i]:
            ret += solve(i)
    dp[v] = ret
    return ret
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
solve(r)
for _ in range(q):
    a = int(input())
    print(dp[a])