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
def kruskal():
    edges = 0
    dist = 0
    while True:
        if edges == n-1: break
        if not graph: return all+1
        u, ve, w = graph.pop()
        if find(u) != find(ve):
            union(u, ve)
            dist += w
            edges += 1
    return dist

n = int(input())
unionfind = [i for i in range(n)]
graph = []
all = 0
for i in range(n):
    s = input().rstrip()
    for j in range(n):
        if s[j] == '0': continue
        if s[j].isupper():
            graph.append((i, j, ord(s[j]) - 38))
            all += ord(s[j]) - 38
        else:
            graph.append((i, j, ord(s[j]) - 96))
            all += ord(s[j]) - 96
graph.sort(reverse=True,key=lambda x:x[2])
print(all - kruskal())