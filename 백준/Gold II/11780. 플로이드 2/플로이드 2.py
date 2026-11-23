import sys

input = sys.stdin.readline
print = sys.stdout.write

INF = float('inf')
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

n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
path = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
floyd_warshall()
for i in dist[1:]:
    for j in i[1:]:
        if j >= INF: print("0 ")
        else: print(str(j)+" ")
    print("\n")
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or dist[i][j] == INF: 
            print("0\n")
            continue
        tmp = []
        getPath(i, j)
        tmp.append(j)
        print(str(len(tmp))+" ")
        for k in tmp:
            print(str(k)+" ")
        print("\n")