import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n-1)]
    colors = [[-1] * n for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            colors[i][j] = colors[j][i] = lines[i][j-(i+1)]
    ret = n*(n-1)*(n-2)//3
    for i in colors:
        a, b = i.count(1), i.count(0)
        ret -= a*b
    print(str(ret//2))
    print("\n")