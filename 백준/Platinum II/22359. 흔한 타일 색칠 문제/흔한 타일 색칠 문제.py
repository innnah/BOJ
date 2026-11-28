import sys
input = sys.stdin.readline

def solve(x, y, s, bx, by, num):
    if s == 2:
        for i in range(2):
            for j in range(2):
                arr[y+i][x+j] = num
        arr[by][bx] = 1
        return
    mid1 = x + s//2
    mid2 = y + s//2
    k = (by >= mid2)*2 + (bx >= mid1)
    for i in range(2):
        for j in range(2):
            arr[mid2-1+i][mid1-1+j] = 1
            if k == i*2+j:
                solve(x+j*(s//2), y+i*(s//2), s//2, bx, by, 2 + (not 1 <= i*2+j <= 2))
            else:
                solve(x+j*(s//2), y+i*(s//2), s//2, mid1-1+j, mid2-1+i, 2 + (not 1 <= i*2+j <= 2))

t, n = map(int, input().split())
n = 2**n
for _ in range(t):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr = [[-1 for _ in range(n)] for _ in range(n)]
    arr[a][b] = 0
    solve(0, 0, n, b, a, 2)
    arr[a][b] = "@"
    for i in range(n):
        for j in range(n):
            if arr[i][j] != "@":
                arr[i][j] = chr(96+arr[i][j])
    for i in arr:
        print(''.join(i))