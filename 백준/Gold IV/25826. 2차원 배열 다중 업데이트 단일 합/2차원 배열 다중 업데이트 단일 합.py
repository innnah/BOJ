import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m-1):
    _, x1, y1, x2, y2, k = map(int, input().split())
    arr2[x2][y2] += k
    arr2[x1-1][y1-1] += k
    arr2[x1-1][y2] -= k
    arr2[x2][y1-1] -= k
for i in range(n-2, -1, -1):
    arr2[n-1][i] += arr2[n-1][i+1]
    arr2[i][n-1] += arr2[i+1][n-1]
for i in range(n-2, -1, -1):
    for j in range(n-2, -1, -1):
        arr2[i][j] += arr2[i+1][j] + arr2[i][j+1] - arr2[i+1][j+1]
_, x1, y1, x2, y2 = map(int, input().split())
ans = 0
for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        ans += arr[i][j] + arr2[i][j]
print(ans)