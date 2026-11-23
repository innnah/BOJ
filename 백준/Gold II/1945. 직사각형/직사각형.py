import sys
input = sys.stdin.readline

n = int(input())
tan_value = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    tan_value.append((y1/x2, 1))
    tan_value.append((y2/x1, -1))
tan_value.sort(key = lambda x:(x[0], -x[1]))
v = 0
ret = 0
for i in range(2*n):
    v += tan_value[i][1]
    ret = max(ret, v)
print(ret)