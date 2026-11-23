import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()
ret, k = 0, 0
a = 0
for i in range(1, l[-1]+1):
    while l[k] < i: k += 1
    if ret < (n-k)*i:
        ret = (n-k)*i
        a = i
print(ret, a)