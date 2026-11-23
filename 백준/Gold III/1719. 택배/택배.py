import sys

input = sys.stdin.readline
print = sys.stdout.write

INF = 987654321
def floyd_warshall():
    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k

def getPath(s, e):
    prev = path[s][e]
    if prev == INF:
        tmp.append(s)
        return
    if s == prev:
        tmp.append(s)
        return
    getPath(s, prev)
    getPath(prev, e)

n, m = map(int, input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
path = [[INF] * (n+1) for _ in range(n+1)]
tmp = []
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c
floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: 
            print("- ")
            continue
        tmp = []
        getPath(i, j)
        tmp.append(j)
        print(str(tmp[1])+" ")
    print("\n")