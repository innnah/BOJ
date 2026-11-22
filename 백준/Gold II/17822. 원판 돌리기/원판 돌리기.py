import sys
sys.setrecursionlimit(150000)
from collections import defaultdict
input = sys.stdin.readline

def dfs(a, b, v):
    visited[a][b] = 1
    flag = False
    for i in graph[(a, b)]:
        if not visited[i[0]][i[1]] and dat[i[0]][i[1]] == dat[a][b]:
            flag = True
            dfs(i[0], i[1], v)
    if (a, b) != v:
        dat[a][b] = 0
    else:
        if flag: dat[a][b] = 0
    return flag

n, m, t = map(int, input().split())
graph = defaultdict(list)
for i in range(1, n+1):
    for j in range(m):
        graph[(i, j+1)].append((i, (j+1)%m+1))
        graph[(i, (j+1)%m+1)].append((i, j+1))
for i in range(1, n):
    for j in range(1, m+1):
        graph[(i, j)].append((i+1, j))
        graph[(i+1, j)].append((i, j))
dat = [[0 for _ in range(m+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]
for _ in range(t):
    x, y, z = map(int, input().split())
    for i in range(x, n+1, x):
        if y:
            for _ in range(z): dat[i].append(dat[i].pop(1))
        else:
            for _ in range(z): dat[i].insert(1, dat[i].pop())
    visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
    flag = False
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dat[i][j] != 0:
                flag |= dfs(i, j, (i, j))
    if not flag:
        s = 0
        c = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if dat[i][j] != 0:
                    s += dat[i][j]
                    c += 1
        if c == 0:
            print(0)
            sys.exit(0)
        avg = s / c
        for i in range(1, n+1):
            for j in range(1, m+1):
                if dat[i][j] != 0:
                    if dat[i][j] < avg:
                        dat[i][j] += 1
                    elif dat[i][j] > avg:
                        dat[i][j] -= 1
print(sum([sum(dat[i]) for i in range(1, n+1)]))