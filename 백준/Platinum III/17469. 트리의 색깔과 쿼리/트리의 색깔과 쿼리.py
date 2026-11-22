import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if len(color_set[root1]) > len(color_set[root2]):
        for i in color_set[root2]:
            color_set[root1].add(i)
        unionfind[root2] = root1
    else:
        for i in color_set[root1]:
            color_set[root2].add(i)
        unionfind[root1] = root2

n, q = map(int, input().split())
tree = [-1] + [-1] + [int(input()) for _ in range(n-1)]
colors = [int(input()) for _ in range(n)]
querys = [list(map(int, input().split())) for _ in range(n+q-1)]

unionfind = [i for i in range(n+1)]
color_set = [set([colors[i-1]]) for i in range(n+1)]

ans = []
for i in range(n+q-2, -1, -1):
    if querys[i][0] == 1:
        union(tree[querys[i][1]], querys[i][1])
    else:
        ans.append(len(color_set[find(querys[i][1])]))
for i in range(len(ans)-1, -1, -1):
    print(ans[i])