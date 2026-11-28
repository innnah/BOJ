import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y
        return 1
    return 0

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
arr = list(map(int, input().split()))
for i in range(1, n+1):
    edges.append((0, i, arr[i-1]))
edges.sort(key=lambda x:-x[2])
parent = [i for i in range(n+1)]

ans = 0
cnt = 0
while cnt < n:
    a, b, c = edges.pop()
    if union(a, b):
        cnt += 1
        ans += c
print(ans)