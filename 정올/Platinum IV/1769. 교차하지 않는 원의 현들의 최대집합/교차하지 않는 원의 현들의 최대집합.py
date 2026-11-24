import sys
input = sys.stdin.readline

d = [[0] * 101 for _ in range(101)]
g = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1
for i in range(1, 101):
    for j in range(i, 0, -1):
        for k in range(j, i+1):
            d[j][i] = max(d[j][i], d[j][k]+d[k][i]+g[j][i])
print(d[1][100]//2)