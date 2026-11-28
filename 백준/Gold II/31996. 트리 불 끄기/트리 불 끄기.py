import sys
sys.setrecursionlimit(110000)
input = sys.stdin.readline

def dfs(v, p):
    for i in tree[v]:
        if i != p:
            ans.append(i)
            state[v] = not state[v]
            dfs(i, v)
    if p != -1:
        if state[v]:
            ans.append(p)
        else:
            ans.append(p)
            ans.append(v)
            ans.append(p)
            state[p] = not state[p]
    else:
        if state[v]:
            ans.append(tree[v][0])

n, m = map(int, input().split())
state = [-1] + list(map(int, input().rstrip()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
ans = []
dfs(m, -1)
print(len(ans))
print(*ans)