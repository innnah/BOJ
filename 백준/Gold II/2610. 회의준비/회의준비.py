import sys
from collections import defaultdict
input = sys.stdin.readline

def find(v):
    if unionfind[v] != v:
        unionfind[v] = find(unionfind[v])
    return unionfind[v]
def union(a, b):
    a = find(a)
    b = find(b)
    unionfind[b] = a
INF = 987654321
def floyd_warshall():
    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n = int(input())
m = int(input())
unionfind = [i for i in range(n+1)]
dist = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    dist[a][b] = 1
    dist[b][a] = 1
s = defaultdict(list)
for i in range(1, n+1):
    s[find(i)].append(i)
k = len(s)
print(k)
floyd_warshall()
ret = []
for i in s.values():
    rep = 0
    mini = INF
    for j in i:
        maxi = 0
        for d in i:
            maxi = max(dist[j][d], maxi)
        if mini > maxi:
            mini = maxi
            rep = j
    ret.append(rep)
ret.sort()
[print(i) for i in ret]