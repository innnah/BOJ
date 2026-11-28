import sys
input = sys.stdin.readline

def dfs(v):
    if visited[v]: return 0
    visited[v] = 1
    for i in match[v]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = v
            return 1
    return 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    match_matrix = [[0] * 101 for _ in range(101)]
    d = [0 for _ in range(101)]
    for _ in range(m):
        t1, t2, _, *l = map(int, input().split())
        for i in range(t1, t2):
            for j in l:
                match_matrix[i][j] = 1
    match = [[] for _ in range(101)]
    for i in range(101):
        for j in range(101):
            if match_matrix[i][j]:
                match[j].append(i)
    for i in range(101):
        visited = [0 for _ in range(101)]
        dfs(i)
    ret = 0
    cnt = 0
    for i in range(101):
        if d[i] != 0:
            ret = i
            cnt += 1
    if cnt == n:
        print(ret+1)
    else:
        print(-1)