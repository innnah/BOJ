import sys

input = sys.stdin.readline
print = sys.stdout.write

def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] != 0 and dist[k][j] != 0:
                    dist[i][j] = 1

n, m = map(int, input().split())
dist = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
floyd_warshall()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if dist[a][b]: print("-1")
    elif dist[b][a]: print("1")
    else: print("0")
    print("\n")