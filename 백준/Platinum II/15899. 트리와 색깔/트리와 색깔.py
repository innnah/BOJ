import sys
sys.setrecursionlimit(201270)
input = sys.stdin.readline

MOD = 10**9+7
def euler_dfs(v, p):
    global cnt
    start[v] = cnt
    for i in graph[v]:
        if i != p:
            cnt += 1
            euler_dfs(i, v)
    end[v] = cnt

def query(v):
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    while idx <= n:
        tree[idx] += num
        idx += (idx & -idx)

n, m, c = map(int, input().split())
colors = list(map(int, input().split()))
colors = [[colors[i], i+1] for i in range(n)]
colors.sort()

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = [0 for _ in range(n+1)]
end = [0 for _ in range(n+1)]
cnt = 1
euler_dfs(1, -1)

ans = 0
querys = [list(map(int, input().split())) for _ in range(m)]
querys.sort(key = lambda x : x[1])

tree = [0 for _ in range(n+1)]
j = 0
for i in range(m):
    v, k = querys[i]
    while j < n and colors[j][0] <= k:
        color, node = colors[j]
        update(start[node], 1)
        j += 1
    ans += query(end[v]) - (query(start[v]-1) if start[v] > 1 else 0)
    ans %= MOD
print(ans)