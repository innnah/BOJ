import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
for i in range(n):
    if arr[i][0] == 1:
        for j in range(m):
            arr[i][j] = not arr[i][j]

cols = [0 for _ in range(m)]
for i in range(m):
    for j in range(n):
        cols[i] += arr[j][i]

cnt = (max(cols) <= 1)
for i in range(n):
    for j in range(m):
        cols[j] += -2*arr[i][j] + 1
    cnt += (max(cols) <= 1)
    for j in range(m):
        cols[j] -= -2*arr[i][j] + 1
print(cnt)