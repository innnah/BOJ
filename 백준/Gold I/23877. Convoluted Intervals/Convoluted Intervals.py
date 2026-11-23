import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0 for _ in range(m+1)]
b = [0 for _ in range(m+1)]
start = [0 for _ in range(2*m+1)]
end = [0 for _ in range(2*m+1)]
for _ in range(n):
    x, y = map(int, input().split())
    a[x] += 1
    b[y] += 1
for i in range(m+1):
    for j in range(m+1):
        start[i+j] += a[i] * a[j]
        end[i+j] += b[i] * b[j]
ret = 0
for i in range(2*m+1):
    ret += start[i]
    print(ret)
    ret -= end[i]