import sys
input = sys.stdin.readline
dic = {True: "YES", False: "NO"}
def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1
n, m = map(int, input().split())
unionfind = [0]
for i in range(1, n+1):
    unionfind.append(i)
for _ in range(m):
    order = list(map(int, input().split()))
    if order[0] == 0:
        union(order[1], order[2])
    else:
        print(dic[find(order[1]) == find(order[2])])