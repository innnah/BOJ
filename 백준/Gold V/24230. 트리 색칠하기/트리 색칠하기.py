import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def dfs(v, prev):
    visited[v] = 1
    equal = 1
    ret = 0
    for i in tree[v]:
        if not visited[i]:
            equal_sub, minimum = dfs(i, v)
            if not equal_sub or colors[i] != colors[v]:
                equal = 0
            ret += minimum
    if equal:
        return (1, colors[v] != colors[prev])
    else:
        return (0, ret + (colors[v] != colors[prev]))

n = int(input())
colors = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(int(dfs(1, 0)[1]))