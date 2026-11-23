import sys, bisect
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(n)]
tmp.sort(key = lambda x : x[1])
x, a, mul = [], [], []
for i in tmp:
    a.append(i[0])
    x.append(i[1])
    mul.append(i[0] * i[1])
for i in range(1, n):
    a[i] += a[i-1]
    mul[i] += mul[i-1]
a.append(0) # a[-1] = 0
mul.append(0)
for _ in range(m):
    query = int(input())
    idx = bisect.bisect(x, query)
    ret = query * a[idx-1] - mul[idx-1]
    ret += mul[-2] - mul[idx-1] - query * (a[-2] - a[idx-1])
    print(ret)