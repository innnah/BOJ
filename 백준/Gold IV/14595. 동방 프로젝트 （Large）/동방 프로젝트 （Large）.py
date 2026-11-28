import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
l = [list(map(int, input().split())) for _ in range(m)]
l.sort(key = lambda x:(x[0], -x[1]))
start, end = -1, -1
parts = []
for i in range(m):
    if end < l[i][0]:
        if i != 0:
            parts.append((start, end))
        start, end = l[i]
    elif end < l[i][1]:
        end = l[i][1]
parts.append((start, end))
ret = n
for i in parts:
    ret -= i[1] - i[0]
print(ret)