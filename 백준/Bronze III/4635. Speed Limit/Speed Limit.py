while 1:
    n = int(input())
    if n == -1: break
    l = [list(map(int, input().split())) for _ in range(n)]
    total = l[0][1] * l[0][0]
    for i in range(1, n):
        total += (l[i][1] - l[i-1][1]) * l[i][0]
    print(f"{total} miles")