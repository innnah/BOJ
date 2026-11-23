import sys
sys.setrecursionlimit(10005)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    dp[v][1] = cost[v-1]
    for i in tree[v]:
        if not visited[i]:
            dfs(i)
            dp[v][0] += max(dp[i])
            dp[v][1] += dp[i][0]
def reconstruct(v, selected):
    visited[v] = 1
    if selected: result_set.append(v)
    for i in tree[v]:
        if not visited[i]:
            if selected:
                reconstruct(i, 0)
            else:
                reconstruct(i, dp[i][0] <= dp[i][1])
n = int(input())
cost = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [[0] * 2 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
dfs(1)
print(max(dp[1]))
visited = [0 for _ in range(n+1)]
result_set = []
reconstruct(1, dp[1][1] >= dp[1][0])
result_set.sort()
print(*result_set)