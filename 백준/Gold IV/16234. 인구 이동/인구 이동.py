import sys
from collections import defaultdict
input = sys.stdin.readline

def find(v):
    if unionfind[v[1]][v[0]] != v:
        unionfind[v[1]][v[0]] = find(unionfind[v[1]][v[0]])
    return unionfind[v[1]][v[0]]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    unionfind[r2[1]][r2[0]] = unionfind[r1[1]][r1[0]]
    
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while 1:
    unionfind = [[[j, i] for j in range(n)] for i in range(n)]
    flag = False
    for i in range(n):
        for j in range(n-1):
            if l <= abs(arr[i][j]-arr[i][j+1]) <= r:
                union([j, i], [j+1, i])
                flag = True
    for i in range(n-1):
        for j in range(n):
            if l <= abs(arr[i][j]-arr[i+1][j]) <= r:
                union([j, i], [j, i+1])
                flag = True
    if not flag:
        break
    d = defaultdict(list)
    for i in range(n):
        for j in range(n):
            d[tuple(find([j, i]))].append(arr[i][j])
    for i in d.keys():
        d[i] = [sum(d[i]) // len(d[i])]
    for i in range(n):
        for j in range(n):
            arr[i][j] = d[tuple(find([j, i]))][0]
    cnt += 1
print(cnt)