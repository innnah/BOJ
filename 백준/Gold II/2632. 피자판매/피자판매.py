import sys, bisect
input = sys.stdin.readline

pizza = int(input())
n, m = map(int, input().split())
a = [int(input()) for _ in range(n)] * 2 + [0]
b = [int(input()) for _ in range(m)] * 2 + [0]
for i in range(1, n*2):
    a[i] += a[i-1]
for i in range(1, m*2):
    b[i] += b[i-1]
sum_a = [0]
sum_b = [0]
sum_a.append(a[n-1])
for i in range(1, n):
    for j in range(n):
        sum_a.append(a[j+i-1] - a[j-1])
sum_b.append(b[m-1])
for i in range(1, m):
    for j in range(m):
        sum_b.append(b[j+i-1] - b[j-1])
sum_a.sort()
sum_b.sort()
ret = 0
for i in sum_a:
    x, y = bisect.bisect(sum_b, pizza-i), bisect.bisect_left(sum_b, pizza-i)
    ret += x-y
print(ret)