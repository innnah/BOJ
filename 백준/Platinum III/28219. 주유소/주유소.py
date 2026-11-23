import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(v, p, c):
    if dp[v][c] != -1: return dp[v][c]
    dp[v][c] = c
    for i in graph[v]:
        if i != p:
            if c:
                dp[v][c] += min(dfs(i, v, 0), dfs(i, v, 1))
            else:
                dp[v][c] += dfs(i, v, 1)
    return dp[v][c]

def dfs2(v, p, depth, c, d):
    if c: return True
    if depth == k: return False
    ret = True
    for i in graph[v]:
        if i != p:
            ret = ret and dfs2(i, v, depth+1, c or (d & (1 << (i-1))), d)
    return ret

n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
if k == 1:
    dp = [[-1, -1] for _ in range(n+1)]
    print(min(dfs(1, -1, 1), dfs(1, -1, 0)))
else:
    for i in range(n+1):
        if len(graph[i]) > 2:
            break
    else:
        print(n//(k+1))
        sys.exit(0)
    mn = 1230912409123
    for i in range(2**n):
        bc = 0
        tmp = i
        while tmp > 0:
            if tmp % 2: bc += 1
            tmp //= 2
        ret = True
        for j in range(1, n+1):
            ret = ret and dfs2(j, -1, 0, i & (1 << (j-1)), i)
            if not ret:
                break
        else:
            mn = min(mn, bc)
    print(mn)