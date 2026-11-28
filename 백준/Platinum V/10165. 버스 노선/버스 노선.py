import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lines = []
deleted = [0 for _ in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    if b < a:
        lines.append((a, b+n, i))
    else:
        lines.append((a, b, i))
        lines.append((a+n, b+n, i))
lines.sort(key = lambda x : (x[0], -x[1], x[2]))
start, end, _ = lines[0]
for i in range(1, len(lines)):
    l, r, _ = lines[i]
    if start <= l <= r <= end:
        deleted[lines[i][2]] = 1
    else:
        start, end = l, r
for i in range(m):
    if not deleted[i]:
        print(i+1, end = ' ')