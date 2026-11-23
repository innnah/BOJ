import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(v, x1, x0):
    visited[v] = 1
    exp[v] = [x1, x0]
    for i, d in graph[v]:
        if visited[i]:
            sum_exp = [exp[v][0]+exp[i][0], exp[v][1]+exp[i][1]]
            if sum_exp[0] == 0:
                if sum_exp[1] != d:
                    print("No")
                    sys.exit(0)
            else:
                if (d-sum_exp[1]) % sum_exp[0] != 0:
                    print("No")
                    sys.exit(0)
                else:
                    exp[v][0] = 0
                    exp[v][1] += (d-sum_exp[1]) // sum_exp[0]
                    exp[i][0] = 0
                    exp[i][1] += (d-sum_exp[1]) // sum_exp[0]
        else:
            dfs(i, -x1, d-x0)
def dfs2(v, value):
    visited[v] = 1
    exp[v] = [0, value]
    for i, d in graph[v]:
        if visited[i]:
            if exp[v][1] + exp[i][1] != d:
                print("No")
                sys.exit(0)
        else:
            dfs2(i, d-exp[v][1])

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
exp = [[0, 0] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
dfs(1, 1, 0)
for i in range(1, n+1):
    exp[i].append(1)
    if exp[i][0] == 0:
        for j in range(1, i+1):
            exp[j].pop()
        visited = [0 for _ in range(n+1)]
        dfs2(i, exp[i][1])
        print("Yes")
        for j in range(1, n+1):
            print(exp[j][1], end = ' ')
        break
else:
    for i in range(1, n+1):
        if exp[i][0] == -1:
            exp[i][0] *= -1
            exp[i][1] *= -1
            exp[i][2] *= -1
    newexp = sorted(exp, key = lambda x : [-x[0], -x[1]])
    x = -newexp[n//2][1]
    print("Yes")
    for i in range(1, n+1):
        print((x + exp[i][1]) * exp[i][2], end = ' ')