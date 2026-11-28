import sys
input = sys.stdin.readline

n, q = map(int, input().split())
cringe = [[0 for _ in range(n+2)] for _ in range(6)]
for _ in range(q):
    x, *y = map(int, input().split())
    if x == 1:
        a, b = y
        cringe[a][b] += 1
        cringe[a+1][b] += 1
        cringe[a-1][b] += 1
        cringe[a][b+1] += 1
        cringe[a][b-1] += 1
    elif x == 2:
        a = y[0]
        mn = max(cringe[a][1:n+1])
        for j in range(1, n+1):
            if cringe[a][j] == mn:
                print(j)
                break

mn = max([max(cringe[i][1:n+1]) for i in range(1, 5)])
for i in range(1, 5):
    for j in range(1, n+1):
        if cringe[i][j] == mn:
            print(i, j)
            sys.exit()