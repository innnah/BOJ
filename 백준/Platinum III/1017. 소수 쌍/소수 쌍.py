import sys
sys.setrecursionlimit(100500)
input = sys.stdin.readline

isPrime = [1 for _ in range(2001)]
def sieve(n):
    isPrime[0] = 0
    isPrime[1] = 0
    m = int(n**0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0
def dfs(v, k):
    if visited[v]: return 0
    visited[v] = 1
    for i in match[v]:
        if i in (0, k): continue
        if d[i] == -1 or dfs(d[i], k):
            d[i] = v
            d[v] = i
            return 1
    return 0
n = int(input())
l = list(map(int, input().split()))
d = [-1 for _ in range(n)]
match = [[] for _ in range(n)]
results = []
sieve(2000)
for i in range(n):
    for j in range(n):
        if i != j:
            if isPrime[l[i]+l[j]]:
                match[i].append(j)
for k in match[0]:
    d[k] = 0
    d[0] = k
    for i in range(1, n):
        if d[i] != -1: continue
        visited = [0 for _ in range(n)]
        dfs(i, k)
    if d.count(-1) == 0:
        results.append(l[k])
    d = [-1 for _ in range(n)]
if len(results) == 0:
    print(-1)
else:
    print(*list(sorted(results)))