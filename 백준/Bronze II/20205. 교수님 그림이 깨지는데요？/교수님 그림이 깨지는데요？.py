n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
large = [[0] * (n*m) for _ in range(n*m)]
for i in range(n):
    for j in range(n):
        for k in range(m):
            for a in range(m):
                large[i*m+k][j*m+a] = l[i][j]
for i in large:
    print(*i)