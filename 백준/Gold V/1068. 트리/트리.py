import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v):
    global ret
    visited[v] = 1
    isLeaf = v != n
    for i in graph[v]:
        if i != delete and not visited[i]:
            isLeaf = 0
            dfs(i)
    if isLeaf: ret += 1

n = int(input())
l = list(map(int, input().split()))
delete = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
ret = 0
root = -1
for i in range(n):
    if l[i] != -1:
        graph[i].append(l[i])
        graph[l[i]].append(i)
    else:
        root = i
graph[n].append(root)
dfs(n)
print(ret)