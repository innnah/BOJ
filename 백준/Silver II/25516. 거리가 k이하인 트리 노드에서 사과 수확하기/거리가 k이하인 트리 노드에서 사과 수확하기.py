import sys
sys.setrecursionlimit(120000)
input = sys.stdin.readline

def dfs(v, p, d):
    if d == k: return arr[v]
    ret = arr[v]
    for i in tree[v]:
        if i != p:
            ret += dfs(i, v, d+1)
    return ret

n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
arr = list(map(int, input().split()))
print(dfs(0, -1, 0))