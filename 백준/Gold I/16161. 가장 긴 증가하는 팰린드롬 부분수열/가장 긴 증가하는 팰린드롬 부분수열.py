import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
a = [[arr[i], i] for i in range(n)]
b = [a[0]]
for i in range(1, n):
    if a[i-1][0] != a[i][0]:
        b.append(a[i])
if len(b) == 1:
    print(min(n, 2))
    sys.exit(0)
m = []
if b[0][0] > b[1][0]:
    m.append([i for i in range(b[1][1])])
for i in range(1, len(b)-1):
    if b[i-1][0] < b[i][0] and b[i][0] > b[i+1][0]:
        m.append([i for i in range(b[i][1], b[i+1][1])])
if b[-2][0] < b[-1][0]:
    m.append([i for i in range(b[-1][1], n)])
ret = 1 + (len(b) != n)
for i in m:
    if len(i) == 1:
        i1 = i2 = i[0]
        while i1 >= 0 and i2 < n and arr[i1] == arr[i2]:
            if i1 >= 1 and i2 < n-1:
                if arr[i1-1] >= arr[i1] or arr[i2+1] >= arr[i2]:
                    i1 -= 1
                    i2 += 1
                    break
            i1 -= 1
            i2 += 1
        ret = max(ret, i2-i1-1)
    elif len(i) == 2:
        i1, i2 = i
        while i1 >= 0 and i2 < n and arr[i1] == arr[i2]:
            if i1 >= 1 and i2 < n-1:
                if arr[i1-1] >= arr[i1] or arr[i2+1] >= arr[i2]:
                    i1 -= 1
                    i2 += 1
                    break
            i1 -= 1
            i2 += 1
        ret = max(ret, i2-i1-1)
    else:
        ret = max(ret, 2)
print(ret)