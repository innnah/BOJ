import sys
sys.setrecursionlimit(201270)
input = sys.stdin.readline

def dfs1(v, p):
    for nxt in tree[v]:
        if nxt == p:
            continue
        dfs1(nxt, v)
        cnt[v] += cnt[nxt]
    if len(tree[v]) >= 3:
        cnt[v] += 1

def dfs2(v, p):
    for nxt in tree[v]:
        if nxt == p:
            continue
        dfs2(nxt, v)
    ans.append(v)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = [0 for _ in range(n+1)]
dfs1(1, -1)
for i in range(1, n+1):
    tree[i].sort(key=lambda x:-cnt[x])

ans = []
dfs2(1, -1)
print(*ans)