import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    rev_graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        rev_graph[b].append(a)
        indegree[b] += 1
    target = int(input())
    
    ret = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        ret.append(v)
        for i in graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    dp = [0 for _ in range(n+1)]
    for i in ret:
        if rev_graph[i]:
            dp[i] = l[i] + dp[max(rev_graph[i], key = lambda x : dp[x])]
        else:
            dp[i] = l[i]
    print(dp[target])