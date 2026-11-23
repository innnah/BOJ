import sys
input = sys.stdin.readline

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1
n = int(input())
m = int(input())
unionfind = [i for i in range(n+1)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j]:
            union(i+1, j+1)
travel = list(map(int, input().split()))
for i in range(1, m):
    if find(travel[i]) != find(travel[i-1]):
        print("NO")
        break
else:
    print("YES")