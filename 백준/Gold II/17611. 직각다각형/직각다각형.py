import sys
input = sys.stdin.readline

n = int(input())
coordx = [0 for _ in range(1000002)]
coordy = [0 for _ in range(1000002)]
l = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    a, b = l[i], l[i-1]
    if a[0] == b[0]:
        if a[1] < b[1]:
            coordy[a[1]+500000] += 1
            coordy[b[1]+500000] -= 1
        else:
            coordy[a[1]+500000] -= 1
            coordy[b[1]+500000] += 1
    else:
        if a[0] < b[0]:
            coordx[a[0]+500000] += 1
            coordx[b[0]+500000] -= 1
        else:
            coordx[a[0]+500000] -= 1
            coordx[b[0]+500000] += 1
for i in range(1000001):
    coordx[i] += coordx[i-1]
    coordy[i] += coordy[i-1]
print(max(max(coordx), max(coordy)))