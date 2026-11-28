import sys
sys.setrecursionlimit(10500)
input = sys.stdin.readline

def dfs_dp(v):
    visited[v] = 1
    for i, d in tree[v]:
        if not visited[i]:
            dp[i] = dp[v] + (n-nodes[i]*2)*d
            dfs_dp(i)
def dfs(v, dis):
    visited[v] = 1
    distance[v] = dis
    a = 1
    for i, d in tree[v]:
        if not visited[i]:
            a += dfs(i, dis+d)
    nodes[v] = a
    return a    
while 1:
    n = int(input())
    if n == 0: break
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        tree[a].append((b,c))
        tree[b].append((a,c))
    visited = [0 for _ in range(n)]
    distance = [0 for _ in range(n)]
    nodes = [0 for _ in range(n)]
    dfs(0, 0)
    dp = [0 for _ in range(n)]
    dp[0] = sum(distance)
    visited = [0 for _ in range(n)]
    dfs_dp(0)
    print(min(dp))