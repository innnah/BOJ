import sys
sys.setrecursionlimit(60000)
input = sys.stdin.readline

def dfs(v, curD):
    visited[v] = 1
    for i, d in tree[v]:
        if not visited[i]:
            dis[i] = (curD + d, i)
            dfs(i, curD+d)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
dist = []
visited = [0 for _ in range(n+1)]
dis = [(0, 1) for _ in range(n+1)]
dfs(1, 0)
m1 = max(dis)
dist.append(dis)

visited = [0 for _ in range(n+1)]
dis = [(0, m1[1]) for _ in range(n+1)]
dfs(m1[1], 0)
m2 = max(dis)
dist.append(dis)

visited = [0 for _ in range(n+1)]
dis = [(0, m2[1]) for _ in range(n+1)]
dfs(m2[1], 0)
dist.append(dis)
for i in range(1, n+1):
    if i == 1:
        print(m1[0])
    elif i in (m1[1], m2[1]):
        print(m2[0])
    else:
        print(max(dist[0][i], dist[1][i], dist[2][i])[0])