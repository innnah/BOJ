import sys

input = sys.stdin.readline
print = sys.stdout.write

INF = 987654321
def floyd_warshall():
    for k in range(1, n+1):
        dist[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
floyd_warshall()
for i in dist[1:]:
    for j in i[1:]:
        if j < INF:
            print(str(j)+' ')
        else:
            print("0"+' ')
    print("\n")