import sys, bisect
input = sys.stdin.readline

k = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in range(1, n):
    a[i] += a[i-1]
a.append(0)
for i in range(1, m):
    b[i] += b[i-1]
b.append(0)
psum_a = []
psum_b = []
for i in range(n):
    for j in range(i+1):
        psum_a.append(a[i] - a[j-1])
for i in range(m):
    for j in range(i+1):
        psum_b.append(b[i] - b[j-1])
psum_a.sort()
psum_b.sort()
ret = 0
for i in psum_a:
    ret += bisect.bisect(psum_b, k-i) - bisect.bisect_left(psum_b, k-i)
print(ret)