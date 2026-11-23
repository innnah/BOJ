import sys
input = sys.stdin.readline

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1

n, m, k = map(int, input().split())
candies = list(map(int, input().split()))
unionfind = [0]
for i in range(1, n+1):
    unionfind.append(i)

groups = [[] for _ in range(n+1)]
knapsack = []
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
for i in range(1, n+1):
    groups[find(i)].append(i)
for i in range(1, n+1):
    if len(groups[i]) != 0:
        candy = 0
        for j in groups[i]:
            candy += candies[j-1]
        knapsack.append([len(groups[i]), candy])

dp = [[0] * k for _ in range(2)]
if knapsack[0][0] < k: dp[0][knapsack[0][0]] = knapsack[0][1]

for i in range(2, len(knapsack)+1):
    if knapsack[i-1][0] < k: dp[1][knapsack[i-1][0]] = knapsack[i-1][1]
    for j in range(1, k):
        if dp[0][j] != 0:
            dp[1][j] = max(dp[1][j], dp[0][j])
            if j + knapsack[i-1][0] < k:
                dp[1][j+knapsack[i-1][0]] = max(dp[1][j+knapsack[i-1][0]], dp[0][j] + knapsack[i-1][1])
    dp[0] = dp[1]
    dp[1] = [0 for _ in range(k)]

print(max(dp[0]))