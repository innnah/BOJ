import sys, heapq
input = sys.stdin.readline
sys.setrecursionlimit(350000)
NEGINF = -(10**40)
def dfs(v):
    global ret
    a[v] = score[v]
    pq = []
    for i in tree[v]:
        sub = dfs(i)
        if sub > 0:
            a[v] += sub
            c[v] = max(c[v], c[i])
        else:
            c[v] = max(c[v], b[i])
        heapq.heappush(pq, -b[i])
    b[v] = a[v]
    ret = max(ret, a[v]+c[v])
    while len(pq):
        cand = -heapq.heappop(pq)
        b[v] = max(b[v], cand)
        if len(pq): ret = max(ret, cand-pq[0])
    return a[v]

n = int(input())
score = [0]
tree = [[] for _ in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    score.append(a)
    if b != -1:
        tree[b].append(i+1)
a = [0 for _ in range(n+1)]
b = [0 for _ in range(n+1)]
c = [NEGINF for _ in range(n+1)]
ret = NEGINF
dfs(1)
print(ret)