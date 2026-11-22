import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, p, q = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    dist = [[10**20 for _ in range(p+1)] for _ in range(p+1)]
    for _ in range(q):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)
        dist[b][a] = min(dist[b][a], c)

    for k in range(1, p+1):
        dist[k][k] = 0
        for i in range(1, p+1):
            for j in range(1, p+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    ans = 10**20
    g = 0
    for i in range(1, p+1):
        cand = 0
        for j in range(n):
            cand += dist[arr[j]][i] ** 2
        if cand < ans:
            ans = cand
            g = i
    print(g, ans)