import sys
input = sys.stdin.readline

def find(v):
    if v == unionfind[v]: return v
    unionfind[v] = find(unionfind[v])
    return unionfind[v]

def union(u, v):
    r1, r2 = find(u), find(v)
    unionfind[r2] = r1

MOD = 10**9+7
n, m = map(int, input().split())
comb = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    comb[i][0] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
        comb[i][j] %= MOD

cnts = [0 for _ in range(n+1)]
cnts[0] = cnts[1] = 1
for i in range(2, n+1):
    for j in range(i):
        cnts[i] += comb[i-1][j] * cnts[i-j-1]
        cnts[i] %= MOD

unionfind = [i for i in range(n+1)]
groups = n
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        groups -= 1
        union(a, b)
    print(cnts[groups])