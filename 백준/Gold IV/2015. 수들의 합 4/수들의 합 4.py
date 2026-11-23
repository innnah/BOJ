import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

for i in range(1, n):
    l[i] += l[i-1]

cnt = 0
dd = defaultdict(int)
for i in range(n):
    if l[i] == m:
        cnt += 1
    cnt += dd[l[i]-m]
    dd[l[i]] += 1

print(cnt)