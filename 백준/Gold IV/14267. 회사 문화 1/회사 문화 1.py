import sys
sys.setrecursionlimit(100005)
input = sys.stdin.readline

def dfs(v, p):
    np = p + directly_praised[v]
    praised[v] += np
    for i in tree[v]:
        dfs(i, np)

n, m = map(int, input().split())
parent = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for i in range(1, n):
    tree[parent[i]].append(i+1)
directly_praised = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    directly_praised[a] += b
praised = [0 for _ in range(n+1)]
dfs(1, 0)
print(*praised[1:])