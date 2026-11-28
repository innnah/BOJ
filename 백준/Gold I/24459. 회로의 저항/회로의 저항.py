import sys
sys.setrecursionlimit(100020)
input = sys.stdin.readline

INF = 10**100
def select(a, b):
    s = a+b
    s.sort()
    return s[:2]
def dfs_min(v, cur_dis):
    global best
    visited[v] = 1
    sub = 0
    sub_min_dis = [INF, INF]
    for i, d in tree[v]:
        if not visited[i]:
            sub += 1
            cand = dfs_min(i, cur_dis+d)
            sub_min_dis = select(sub_min_dis, cand)
    if sub == 0:
        #print(v, cur_dis)
        return [cur_dis, INF]
    if sub >= 2:
        #print(v, sub_min_dis, cur_dis)
        sub_min_dis[0] -= cur_dis
        sub_min_dis[1] -= cur_dis
        if len(tree[0]) == 1:
            best = min(best, cur_dis + sub_min_dis[0])
        best = min(best, sub_min_dis[1] + sub_min_dis[0])
        return [sub_min_dis[0] + cur_dis, sub_min_dis[1] + cur_dis]
    if len(tree[0]) == 1:
        best = min(best, sub_min_dis[0])
    #print(v, sub_min_dis)
    return sub_min_dis
def dfs_max(v, cur_dis):
    visited[v] = 1
    distance[v] = cur_dis
    for i, d in tree[v]:
        if not visited[i]:
            dfs_max(i, cur_dis+d)

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [0 for _ in range(n)]
distance = [0 for _ in range(n)]
dfs_max(0, 0)
max_node, max_dis = -1, 0
for i in range(n):
    if distance[i] > max_dis:
        max_node, max_dis = i, distance[i]
visited = [0 for _ in range(n)]
distance = [0 for _ in range(n)]
dfs_max(max_node, 0)
print(max(distance))

visited = [0 for _ in range(n)]
best = INF
dfs_min(0, 0)
print(best)